from django.db import models
from django.contrib.auth.models import User

#News on site
class BlogNews(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    text = models.TextField()

    class Meta:
        verbose_name_plural  = "News"

    def __str__(self):
        return self.title

#Category for Posts
class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name;



#Posts
class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE,)
    title = models.CharField(max_length=200)
    date = models.DateTimeField()
    image = models.ImageField(upload_to="images/")
    text = models.TextField()
    post_by = models.ForeignKey(User, on_delete=models.CASCADE,)

    class Meta:
        verbose_name_plural  = "Post"

    def __str__(self):
        return self.title

    def summary(self):
        return self.text[:70]
