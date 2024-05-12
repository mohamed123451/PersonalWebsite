from django.shortcuts import render
from .models import Blog

# Create your views here.
def allBlogs(request):
    blogs = Blog.objects.order_by('-date')

    context = {
        'blogs': blogs
    }

    return render(request, 'allblogs.html', context)