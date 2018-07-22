from django.shortcuts import render
from .models import BlogNews

def home(request):
    news = BlogNews.objects
    return render(request, 'blog/home.html', {'news':news})
