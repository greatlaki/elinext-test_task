from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,)

from .views import *


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path('profile-user/', ProfileListAPIView.as_view(), name='profile-user'),
    path('profile-user/<int:id>', ProfileDetailAPIView.as_view(), name='profile-user'),
    path('username-verify/', VerifyUsername.as_view(), name='username-verify'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

