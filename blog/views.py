from django.shortcuts import render, redirect, reverse, get_object_or_404
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
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            messages.success(request, 'Successfully added a blog post!')
            return redirect(reverse('detail_post', args=[post.slug]))
        else:
            messages.error(request, 'Failed to add the blog post. Please ensure the form is valid.')
    else:
        form = PostForm()

    template = 'blog/add_blog.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_blog(request, slug):
    """ Edit a Blog Post """
    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated blog post!')
            return redirect(reverse('detail_post', args=[post.slug]))
        else:
            messages.error(request, 'Failed to update blog post. Please ensure the form is valid.')
    else:
        form = PostForm(instance=post)
        messages.info(request, f'You are editing {post.title}')

    template = 'blog/edit_blog.html'
    context = {
        'form': form,
        'post': post,
    }

    return render(request, template, context)


def delete_blog(request, slug):
    """ Delete a blog post from the blog """
    blog = get_object_or_404(Post, slug=slug)
    blog.delete()
    messages.success(request, 'Blog post deleted!')
    return redirect(reverse('detail_post'))
