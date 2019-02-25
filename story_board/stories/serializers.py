from rest_framework import serializers

from .models import Author, Story


class AuthorSerializer(serializers.ModelSerializer):
	"""docstring for AuthorSerializer"""
	class Meta:
		fields = (
			'id',
			'user',
			'followers',
			'following',
			'author_slug',
		)
		model =  Author


class StorySerializer(serializers.ModelSerializer):
	"""docstring for StorySerializer"""
	class Meta:
		fields = (
			'id',
			'title',
			'body',
			'author',
			'recommendations',
			'published',
		)
		model =  Story