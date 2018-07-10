from django.db import models

class Portfolio(models.Model):
    title = models.CharField(max_length=200)
