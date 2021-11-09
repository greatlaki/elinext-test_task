from django.urls import path

from .views import *


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('username-verify/', VerifyUsername.as_view(), name='username-verify'),
]

