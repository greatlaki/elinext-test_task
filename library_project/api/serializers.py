from rest_framework import serializers

from .models import *


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=69, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password',
                  'first_name', 'last_name',
                  'phone_number', 'photo']

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
