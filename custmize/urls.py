from django.urls import path
from .views import create_blog_post

urlpatterns = [
    path("",create_blog_post),
]
