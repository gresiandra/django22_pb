from django.shortcuts import render, get_object_or_404
from .models import blog

def allblogs(request):

    # retrieve all data from model called 'blog'
    blogs = blog.objects.all()
    
    context = {
        'blogs':blogs,
    }
    return render(request, 'blog/blog.html', context)

def detail(request, blog_id):

    # get_object_or_404(model_name, primary_key as pk = parameter) 

    blogdetail = get_object_or_404(blog, pk=blog_id)

    context = {
        'blogs':blogdetail
    }
    return render(request, 'blog/detail.html', context)