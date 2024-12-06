from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

    def create(self, validated_data):
        user = User(
            email=validated_data.get('email'),
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Post
        fields = ('id', 'author', 'title', 'content', 'created_at')
