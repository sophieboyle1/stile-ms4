from django.shortcuts import render, redirect
from .models import Category, Post
from django.contrib import messages

from .forms import CommentForm
from .forms import PostForm


def post(request):
    posts = Post.objects.all()

    template = 'blog/blog.html'
    context = {
        'posts': posts,
    }

    return render(request, template, context)


def detail_post(request, slug):
    post = Post.objects.get(slug=slug)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.post = post
            obj.save()
            return redirect('detail_post', slug=post.slug)
    else:
        form = CommentForm()

    template = 'blog/blog_detail.html'
    context = {
        'post': post,
        'form': form,
    }

    return render(request, template, context)


def category(request, slug):
    category = Category.objects.get(slug=slug)

    template = 'blog/blog_category.html'
    context = {
        'category': category
    }

    return render(request, template, context)


def add_blog(request):
    """ Add a blog post to the blog """
    form = PostForm()
    template = 'blog/add_blog.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
