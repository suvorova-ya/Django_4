#import django_filters
from django_filters import FilterSet, CharFilter, ModelChoiceFilter, DateFilter
from .models import Post, Author


# создаем фильтр
class PostFilter(FilterSet):
       class Meta:
        model = Post
        fields = {
        'dateCreation': ['gt'],
        'title': ['icontains'],
        'author': ['exact'],
        }
