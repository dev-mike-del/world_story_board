from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth import logout, login

from accounts.views import register

app_name = 'account'

urlpatterns = [
    path('register/', register, name='register'),
    path('logout/', logout, {'next_page': '/'}, name='logout'),
    path('login/', login, {'template_name': 'accounts/login.html'}, name='login'),
]