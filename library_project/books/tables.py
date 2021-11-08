import django_tables2 as tables
import django_filters

from .models import *


class BookTable(tables.Table):
    class Meta:
        model = Book
        template_name = "django_tables2/bootstrap.html"
        fields = ('birth_year', 'author', 'title', 'written_year')


class BookFilter(django_filters.FilterSet):
    class Meta:
        model = Book
        fields = ('birth_year', 'author', 'title', 'written_year')
