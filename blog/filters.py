from .models import Post
import django_filters
from django import forms

class PostFilter(django_filters.FilterSet):
    class Meta:
        model = Post
        fields = {'title': ['icontains'],}
        labels = {'title': 'Search',}
