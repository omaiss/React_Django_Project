from rest_framework import serializers
from .models import User, Custom_User

class UserViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'is_verified']

class UserAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class CustomUserAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Custom_User
        fields = ['full_name', 'email', 'position', 'job', 'department']
        