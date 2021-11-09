from django.contrib import auth
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed


from .models import *


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=69, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password']

    def validate(self, attrs):
        username = attrs.get('username', '')
        first_name = attrs.get('first_name', '')
        last_name = attrs.get('last_name', '')

        if not username.isalnum():
            raise serializers.ValidationError(
                self.default_error_messages)

        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class UserVerificationSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=555)

    class Meta:
        model = User
        fields = ['token']


class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=68, min_length=6, write_only=True)
    username = serializers.CharField(
        max_length=255, min_length=3, read_only=True)

    tokens = serializers.SerializerMethodField()

    def get_tokens(self, obj):
        user = User.objects.get(username=obj['username'])

        return {
            'refresh': user.tokens()['refresh'],
            'access': user.tokens()['access'],
        }

    class Meta:
        model = User
        fields = ['password', 'username', 'tokens']


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ['id', 'first_name', 'last_name', 'phone_number', 'photo']

