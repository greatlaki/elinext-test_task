from django.urls import path

from .views import *


urlpatterns = [
    path('', menu_view, name='home'),
    path('addbook/', book_upload, name='add_book'),
    # path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('table/', FilteredBookListView.as_view(), name='tables'),
]