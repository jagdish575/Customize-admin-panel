from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    date_created=models.DateTimeField( auto_now_add=True)
    last_modified = models.DateTimeField( auto_now_add=True)
    is_draft =models.BooleanField(default=True)