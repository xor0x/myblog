from django.db import models

class BlogNews(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    text = models.TextField()

    class Meta:
        verbose_name_plural = "News"


    def __str__(self):
        return self.title
