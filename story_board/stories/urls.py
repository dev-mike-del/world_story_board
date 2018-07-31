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
from django.urls import path

from .views import (
    Story_List, Author_Story_List, 
)

app_name = 'stories'

urlpatterns = [
    
    path(
        '',
        Story_List.as_view(),
        name="story_list"
    ),
    path(
        '<slug:author_slug>',
        Author_Story_List.as_view(),
        name="author_story_list"
    ),
]