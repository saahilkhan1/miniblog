from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Blog, Like, Comment

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class BlogSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=True)
    content = serializers.CharField(required=True)
    
    class Meta:
        model = Blog
        fields = '__all__'
        read_only_fields = ['author']

class LikeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Like
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = '__all__'
