from django.urls import path

from .views import *


urlpatterns = [
    path('', BookListView.as_view(), name='home'),
    path('addbook/', book_upload, name='add_book'),
    path('login/', LoginUser.as_view(), name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('logout/', logout_user, name='logout'),

]