from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'groups']
# Refactor to AbstractBaseUser and include       
# 'current_room', 'health_pts', 'phrase' needed for character


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['name']
