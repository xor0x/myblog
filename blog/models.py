from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from ckeditor_uploader.fields import RichTextUploadingField


class SiteSettings(models.Model):
    site_title = models.CharField(max_length=200)
    site_email = models.CharField(max_length=200)

    def __str__(self):
        return self.site_title




#News on site start
class BlogNews(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    text = RichTextUploadingField()
    link = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural  = "News"

    def __str__(self):
        return self.title
#News on site end


#Category for Posts start
class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'


    def __str__(self):
        return self.name;
#Category for Posts end


#Posts start
class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE,)
    title = models.CharField(max_length=200)
    date = models.DateTimeField()
    image = models.ImageField(upload_to="images/")
    text = RichTextUploadingField()
    watch_total = models.IntegerField(default=1)
    post_by = models.ForeignKey(User, on_delete=models.CASCADE,)

    class Meta:
        verbose_name_plural  = "Post"

    def __str__(self):
        return self.title

    def summary(self):
        return self.text[:200]
#Posts start end
