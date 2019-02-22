from rest_framework import serializers

from .models import Author, Story


class AuthorSerializer(serializers.ModelSerializer):
	"""docstring for AuthorSerializer"""
	class Meta:
		fields = (
			'id',
			'user',
			'followrs',
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
			'story_slug',
			'published',
			'date_created',
			'date_modified',
		)
		model =  Story