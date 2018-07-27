from django.urls import path

from accounts.views import register

app_name = 'account'

urlpatterns = [
    path('register/', register, name='register'),
]