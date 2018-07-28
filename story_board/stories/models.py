from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

class Story(models.Model):
    """docstring for Story"""
    title = models.CharField(max_length=200)
    body = models.TextField(max_length=2000)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    recommendations = models.ManyToManyField(
        User, related_name='recommendations', blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("stories:list")