from django.urls import path
from django.contrib.auth import views as auth_views

from accounts.views import register

app_name = 'account'

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', auth_views.login, {'template_name': 'accounts/login.html'}, name='login'),
]