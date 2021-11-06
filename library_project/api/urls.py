from django.urls import path
from rest_framework.authtoken import views

from .views import *


urlpatterns = [
    path('', BookApiView.as_view()),
    path('login/', LoginUser.as_view()),
    path('register/', RegisterUser.as_view(), name='auth_register'),
    path('logout/', user_logout),
    path('user/', UserView.as_view()),
    path('api-token-auth/', views.obtain_auth_token),
]

