from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from .models import User, Profile


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'username', 'password')


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'username')


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username')

    class Meta:
        model = Profile
        fields = ['id', 'username', 'user', 'profile_pic', 'cover_pic', 'fullname', 'position', 'bio',
                  'user_profile_pic', 'user_cover_pic']
        read_only_fields = ['user']

    def get_username(self, user):
        username = user.user.username
        return username
