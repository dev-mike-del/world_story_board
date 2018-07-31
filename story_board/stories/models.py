import itertools
import uuid

from django.contrib.auth import get_user_model
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

User = get_user_model()


class Author(models.Model):
    """docstring for Post"""
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,)
    bio = models.TextField(max_length=500, blank=True)
    followers = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='followers', blank=True,)
    following = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='following', blank=True,)
    author_slug = models.SlugField(unique=True, default=uuid.uuid4, max_length=255)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse("stories:author_story_list")

    def save(self, *args, **kwargs):
        max_length = Author._meta.get_field('author_slug').max_length
        self.author_slug = orig = slugify(self)[:max_length]

        for x in itertools.count(1):
            if not Author.objects.filter(author_slug=self.author_slug).exists():
                break
            self.author_slug = "%s-%d" % (orig[:max_length - len(str(x)) - 1], x)


        super(Author, self).save(*args, **kwargs)


class Story(models.Model):
    """docstring for Story"""
    title = models.CharField(max_length=200)
    body = models.TextField(max_length=2000)
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, blank=True, null=True)
    recommendations = models.ManyToManyField(
        User, related_name='recommendations', blank=True)
    story_slug = models.SlugField(unique=True, default=uuid.uuid4, max_length=255)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("stories:list")

    def save(self, *args, **kwargs):
        max_length = Story._meta.get_field('story_slug').max_length
        self.story_slug = orig = slugify(self)[:max_length]

        for x in itertools.count(1):
            if not Story.objects.filter(story_slug=self.story_slug).exists():
                break
            self.story_slug = "%s-%d" % (orig[:max_length - len(str(x)) - 1], x)


        super(Story, self).save(*args, **kwargs)