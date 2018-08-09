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
    paginator = Paginator(posts,1)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    ctx = {
    'news':news,
    'posts':posts,
    'site_settings':site_settings,
    'categorys':categorys,
    }
    url = 'blog/home.html'
    return render(request, url, ctx)


def detail(request,post_id):
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
    }
    url = 'blog/detail.html'
    return render(request, url, ctx)


def list_of_post_category(request, category_slug):
    categorys = Category.objects.all()
    category = get_object_or_404(Category, slug=category_slug)
    post = Post.objects.filter(category=category)
    ctx = {
    'post':post,
    'category':category,
    'categorys':categorys,
    }
    url = 'blog/post/category.html'
    return render(request, url, ctx)
