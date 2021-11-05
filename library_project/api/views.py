from pytz import unicode
from rest_framework import generics
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from books.models import Book
from .serializers import BookSerializer, RegisterSerializer


class BookApiView(generics.ListAPIView, APIView):
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class RegisterUser(generics.CreateAPIView, APIView):
    permission_classes = (AllowAny,)
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class LoginUser(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'user': unicode(request.user),
            'auth': unicode(request.auth),
        }
        return Response(content)