from rest_framework import serializers

from .models import Author, Story


class AuthorSerializer(serializers.ModelSerializer):
    """docstring for AuthorSerializer"""
    class Meta:
        fields = (
            'username',
            'bio',
            'followers',
            'following',
            'author_slug',
        )
        read_only_fields = ('id',
                            'followers',
                            'following',
                            'author_slug',
                            )
        model = Author


class StorySerializer(serializers.ModelSerializer):
    """docstring for StorySerializer"""

    author = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name='apiv1:author-detail',
    )
    recommendations = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='apiv1:author-detail',
    )

    class Meta:
        fields = (
            'id',
            'title',
            'body',
            'author',
            'recommendations',
            'story_slug',
            'published',
            'date_created',
            'date_modified',
        )
        read_only_fields = ('id',
                            'author',
                            'recommendations',
                            'story_slug',
                            'published',
                            'date_created',
                            'date_modified',
                            )
        model = Story

