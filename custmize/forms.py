from django import forms
from .models import BlogPost
from django_summernote.widgets import SummernoteWidget

class BlogPostForm(forms.ModelForm):
    content = forms.CharField(widget=SummernoteWidget())

    class Meta:
        model = BlogPost
        fields = ['title', 'content']
