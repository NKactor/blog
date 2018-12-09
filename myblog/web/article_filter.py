
from rest_framework import filters

import django_filters

from web.models import Articles, ArticleType


class ArticleFilter(filters.FilterSet):
    title = django_filters.CharFilter('title', lookup_expr='contains')
    desc = django_filters.CharFilter('desc', lookup_expr='contains')
    contents = django_filters.CharFilter('contents', lookup_expr='contains')

    class Meta:
        model = Articles
        fields = ['title', 'desc', 'contents', 'id']


class TypeFilter(filters.FilterSet):

    id = django_filters.CharFilter('art_type', lookup_expr='contains')

    class Meta:
        model = Articles
        fields = ['id']
