from django.urls import path

from .views import *


urlpatterns = [
    path('', BookListView.as_view(), name='home'),
    path('addbook/', book_upload, name='add_book'),
]