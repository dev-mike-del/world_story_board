from django.contrib import admin

from .models import Author, Story

class StoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date_created', 'date_modified')
    list_display_links = ('id', 'title', 'date_created', 'date_modified')


admin.site.register(Author)
admin.site.register(Story, StoryAdmin)
