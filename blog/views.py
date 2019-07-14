from django.shortcuts import render, get_object_or_404
from .models import Blog

blogs = Blog.objects

def allblogs(request):
    return render(request, 'blog/allblogs.html', 
                  {'title': 'Doggie Blog',
                   'blogs': blogs})

def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/blog_detail.html',
                  {'title' : 'Doggie Blog Detail',
                   'blog' : blog})
    