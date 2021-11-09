from django.urls import path

from .views import *


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('profile-user/', ProfileListAPIView.as_view(), name='profile-user'),
    path('profile-user/<int:id>', ProfileDetailAPIView.as_view(), name='profile-user'),
    path('username-verify/', VerifyUsername.as_view(), name='username-verify'),
]

