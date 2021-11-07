from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import *


urlpatterns = [
    path('', BookApiView.as_view()),
    path('user/', user, name='user'),
    path('login/', login_view, name='login'),
    path('token-refresh/', refresh_token_view),
    path('register/', RegisterUser.as_view(), name='auth_register'),
    path('logout/', user_logout),
]

