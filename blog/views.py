from django.shortcuts import render, get_object_or_404
from .models import Blog

blogs = Blog.objects

def allblogs(request):
    blogs = Blog.objects
    return render(request, 'blog/blogs.html', 
                  {'title': 'Doggie Blog',
                   'blogs': blogs})

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html',  
                  {'title' : 'Doggie Blog Detail',
                   'blog' : blog})
    