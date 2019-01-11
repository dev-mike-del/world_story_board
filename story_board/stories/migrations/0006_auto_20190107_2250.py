# Generated by Django 2.0.7 on 2019-01-08 06:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0005_story_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='story',
            name='date_modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]