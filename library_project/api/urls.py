from django.urls import path

from .views import *


urlpatterns = [
    path('', BookApiView.as_view()),
    path('login/', LoginUser.as_view()),
    path('register/', RegisterUser.as_view(), name='auth_register'),
]