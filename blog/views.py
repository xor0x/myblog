from django.shortcuts import render, get_object_or_404
from .models import BlogNews, Post, Category, SiteSettings
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

def home(request):
    site_settings = SiteSettings.objects.all()
    news = BlogNews.objects
    posts = Post.objects.get_queryset().order_by('id')
    paginator = Paginator(posts,1)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'blog/home.html', {'news':news,'posts':posts,'site_settings':site_settings,})


def detail(request,post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/detail.html',{'post':post})
