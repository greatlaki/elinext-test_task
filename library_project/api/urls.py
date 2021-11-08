from django.urls import path

from .views import *


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('username-verify/', VerifyUsername.as_view(), name='username-verify'),
]

