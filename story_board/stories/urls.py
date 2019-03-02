"""story_board URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, path

from .views import (
    Story_List, 
    Author_Story_List,
    Author_Story_Update,
    Following_Story_List,
    About,
    Sitemap,
    Story_Delete,
)

app_name = 'stories'

urlpatterns = [

    path(
        'following',
        Following_Story_List.as_view(),
        name="following_story_list"
    ),
    path(
        'delete/<slug:story_slug>',
        Story_Delete.as_view(),
        name="delete_story"
    ),
    path(
        '',
        Story_List.as_view(),
        name="story_list"
    ),
    path(
        'author/<slug:author_slug>',
        Author_Story_List.as_view(),
        name="author_story_list"
    ),
    path(
        'about',
        About,
        name="about"
    ),
    path(
        'story/<slug:story_slug>',
        Author_Story_Update.as_view(),
        name="author_story_update"
    ),
    path(
        'sitemap',
        Sitemap,
        name="sitemap"
    ),
]