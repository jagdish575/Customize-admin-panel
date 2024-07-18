from typing import Any
from django.contrib import admin
from django.http import HttpRequest
from custmize.models import Blog,Comment
from django.utils import timezone
from django_summernote.admin import SummernoteModelAdmin
#ckedito
    

# Register your models here.
class Blogmanager(SummernoteModelAdmin):
    summernote_fields = '__all__'
    list_display=('title','body','date_created','last_modified','is_draft')
    list_filter = ('is_draft','date_created',)
    ordering =('title','-date_created')
    search_fields =('title',)
    prepopulated_fields ={'slug':('title',)}
    list_per_page=50

    def get_ordering(self, request):
        if request.user.is_superuser:
            return ('title','-date_created')
        return ('title',)
    actions=('set_blog_to_published',)
    date_hierarchy ='date_created'
    fields =( ("title",'slug'),'body','is_draft',)
    


    summernote_fields = ('body',)

    def days_since_creation(self,Blog):
        diff=timezone.now()-Blog.date_created
        return diff.days
    days_since_creation.short_description ='Days active'


    def set_blog_to_published(self,request,queryset):
        count =queryset.update(is_draft=False)
        self.message_user(request,'{} blogs are published succesfully.'.format(count))
    set_blog_to_published.short_description ="Mark selected blogs as  publised"






admin.site.register(Blog,Blogmanager)
admin.site.register(Comment)



