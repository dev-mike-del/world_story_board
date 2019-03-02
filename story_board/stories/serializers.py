from rest_framework import serializers

from .models import Author, Story


class AuthorSerializer(serializers.ModelSerializer):
    """docstring for AuthorSerializer"""

    id = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name='apiv1:author-detail',
    )
    followers = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='apiv1:author-detail',
    )
    following = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='apiv1:author-detail',
    )

    class Meta:
        fields = (
            'id',
            'username',
            'bio',
            'followers',
            'following',
        )
        read_only_fields = ('id',
                            'username',
                            'followers',
                            'following',
                            )
        model = Author


class StorySerializer(serializers.ModelSerializer):
    """docstring for StorySerializer"""

    id = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name='apiv1:story-detail',
    )
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
            'published',
            'date_created',
            'date_modified',
        )
        read_only_fields = ('id',
                            'author',
                            'recommendations',
                            'published',
                            'date_created',
                            'date_modified',
                            )
        model = Story


