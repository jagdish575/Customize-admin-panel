from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    date_created=models.DateTimeField( auto_now_add=True)
    last_modified = models.DateTimeField( auto_now_add=True)
    is_draft =models.BooleanField(default=True)
    slug = models.SlugField(max_length=100)


    def __str__(self):
        return self.title
    
class Comment(models.Model):
    blog = models.ForeignKey("blog", related_name="comments", on_delete=models.CASCADE)
    text = models.TextField()
    is_active = models.BooleanField(default=True)
    date_created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
    