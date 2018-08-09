from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('post/<int:post_id>',views.detail, name='detail'),
    path('post/category/<slug:category_slug>',views.list_of_post_category, name='list_of_post_category'),
    path('portfolio/', include('portfolio.urls')),
    path('account/', include('account.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
