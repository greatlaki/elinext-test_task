from django.contrib import admin

from .models import *


class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'written_year', 'birth_year')
    list_display_links = ('id', 'title', 'author', 'written_year', 'birth_year')
    search_fields = ('title', 'author', 'written_year', 'birth_year')


admin.site.register(Book, BookAdmin)

