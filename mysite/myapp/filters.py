import django_filters
from myapp import models


class BooksFilter(django_filters.FilterSet):
    price_gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt')
    price__lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt')

    class Meta:
        model = models.Book
        fields = ['genre', 'author', 'press', 'price']

