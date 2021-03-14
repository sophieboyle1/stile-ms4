from django.shortcuts import render
from .models import Category, Post, Comment


def post(request):
    template = 'blog/blog.html'

    return render(request, template)
