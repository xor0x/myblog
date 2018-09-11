from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogNews, Post, Category, SiteSettings
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.auth.decorators import login_required
from .forms import CommentForm
from .filters import PostFilter




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
    posts = Post.objects.get_queryset().order_by('-id')
    popular_posts = Post.objects.get_queryset().order_by('watch_total')
    paginator = Paginator(posts,6)
    popular_page = Paginator(popular_posts,5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    ctx = {
    'news':news,
    'posts':posts,
    'site_settings':site_settings,
    'categorys':categorys,
    'popular_posts':popular_posts,
    }
    return render(request, 'blog/home.html', ctx)


def detail(request,pk):
    try:
        site_settings = SiteSettings.objects.get()
    except SiteSettings.DoesNotExist:
        site_settings = None
    categorys = Category.objects.all()
    try:
        news = BlogNews.objects.get()
    except BlogNews.DoesNotExist:
        news = None
    post = get_object_or_404(Post, pk=pk)
    post.watch_total += 1
    post.save()
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


@login_required(login_url="/account/signup")
def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('detail', pk=post.pk)
        else:
            return redirect('detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/detail.html', {'form': form})




def search(request):
    post_list = Post.objects.all()
    post_filter = PostFilter(request.GET, queryset=post_list)
    return render(request, 'blog/search.html', {'filter': post_filter})


def offline(request):
    return render(request, 'blog/offline.html')
