from django.contrib.auth.models import User
from rest_framework import serializers

from .models import (
        Post, 
        Comment, 
        Group, 
        Follow,
    )    


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        fields = ('id', 'text', 'author', 'pub_date',)
        model = Post



class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
            slug_field='username',
            read_only=True
        )
    post = serializers.IntegerField(
            source='post_id', 
            required=False
        )

    class Meta:
        fields = ('id', 'text', 'post', 'author', 'created',)
        model = Comment



class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
            slug_field='username',
            read_only=True,
            default=serializers.CurrentUserDefault()
        )

    following = serializers.SlugRelatedField(
            slug_field='username',
            queryset=User.objects.all()
        )

    class Meta:
        fields = ('user', 'following',)
        model = Follow



class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title',)
        model = Group
