from django.shortcuts import render
from .models import BlogNews, Post, Category

def home(request):
    news = BlogNews.objects
    posts = Post.objects
    return render(request, 'blog/home.html', {'news':news,'posts':posts,})
