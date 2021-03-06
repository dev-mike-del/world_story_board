# Generated by Django 2.0.7 on 2018-07-28 02:47

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0002_auto_20180727_1941'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='author_slug',
            field=models.SlugField(default=uuid.uuid4, max_length=255, unique=True),
        ),
        migrations.AddField(
            model_name='story',
            name='story_slug',
            field=models.SlugField(default=uuid.uuid4, max_length=255, unique=True),
        ),
    ]
