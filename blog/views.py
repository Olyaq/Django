# blog/views.py
from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from django.utils import timezone

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def category_posts(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    posts = Post.objects.filter(category=category, published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/category_posts.html', {'category': category, 'posts': posts})