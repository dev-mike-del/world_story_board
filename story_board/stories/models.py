import datetime
import itertools
import uuid

from django.db.models import Q
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
    username = models.CharField(max_length=200, blank=True)
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
            if self.id:
                if Author.objects.filter(
                        Q(author_slug=self.author_slug),
                        Q(user=self.user)
                ).exists():
                    break
            if not Author.objects.filter(author_slug=self.author_slug).exists():
                break

            # Truncate the original slug dynamically. Minus 1 for the hyphen.
            self.author_slug = "%s-%d" % (orig[:max_length - len(str(x)) - 1], x)

        self.username = self.user.username
        super(Author, self).save(*args, **kwargs)


class Story(models.Model):
    """docstring for Story"""
    title = models.CharField(max_length=200)
    body = models.TextField(max_length=2000)
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, blank=True, null=True)
    recommendations = models.ManyToManyField(
        Author, related_name='recommendations', blank=True)
    story_slug = models.SlugField(unique=True, default=uuid.uuid4, max_length=255)
    published = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("stories:story_list")

    def save(self, *args, **kwargs):
        max_length = Story._meta.get_field('story_slug').max_length
        self.story_slug = orig = slugify(self)[:max_length]

        for x in itertools.count(1):
            if self.id:
                if Story.objects.filter(
                        Q(story_slug=self.story_slug),
                        Q(author=self.author),
                        Q(id=self.id),
                ).exists():
                    break
            if not Story.objects.filter(story_slug=self.story_slug).exists():
                break

            # Truncate the original slug dynamically. Minus 1 for the hyphen.
            self.story_slug = "%s-%d" % (orig[:max_length - len(str(x)) - 1], x)


        super(Story, self).save(*args, **kwargs)

    @property
    def is_posted_today(self):
        if datetime.datetime.today().date() == self.date_modified.date():
            return True
        else:
            return False
