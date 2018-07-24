from django.shortcuts import render, get_object_or_404
from .models import BlogNews, Post, Category

def home(request):
    news = BlogNews.objects
    posts = Post.objects
    return render(request, 'blog/home.html', {'news':news,'posts':posts,})


def detail(request,post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/detail.html',{'post':post})
