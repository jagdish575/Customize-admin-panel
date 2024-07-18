from django.shortcuts import render, redirect
from .forms import BlogPostForm

def create_blog_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    else:
        form = BlogPostForm()
    return render(request, 'create_blog_post.html', {'form': form})
