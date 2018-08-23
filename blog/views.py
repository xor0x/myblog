from django.shortcuts import render, get_object_or_404
from .models import BlogNews, Post, Category, SiteSettings
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


def home(request):
    try:
        site_settings = SiteSettings.objects.get()
    except SiteSettings.DoesNotExist:
        site_settings = None
    try:
        news = BlogNews.objects.get()
    except BlogNews.DoesNotExist:
        news = None
    categorys = Category.objects.all()
    posts = Post.objects.get_queryset().order_by('id')
    paginator = Paginator(posts,6)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    ctx = {
    'news':news,
    'posts':posts,
    'site_settings':site_settings,
    'categorys':categorys,
    }
    return render(request, 'blog/home.html', ctx)


def detail(request,post_id):
    try:
        site_settings = SiteSettings.objects.get()
    except SiteSettings.DoesNotExist:
        site_settings = None
    categorys = Category.objects.all()
    try:
        news = BlogNews.objects.get()
    except BlogNews.DoesNotExist:
        news = None
    post = get_object_or_404(Post, pk=post_id)
    ctx = {
    'post':post,
    'news':news,
    'categorys':categorys,
    'site_settings':site_settings,
    }
    return render(request, 'blog/detail.html', ctx)


def list_of_post_category(request, category_slug):
    try:
        site_settings = SiteSettings.objects.get()
    except SiteSettings.DoesNotExist:
        site_settings = None
    category = get_object_or_404(Category, slug=category_slug)
    post = Post.objects.filter(category=category)
    ctx = {
    'post':post,
    'category':category,
    'site_settings':site_settings,
    }
    return render(request, 'blog/post/category.html', ctx)
