from django.urls import path
from django.contrib.auth import views as auth_views

from rest_framework.authtoken.views import obtain_auth_token

from accounts.views import register, api_token_register

app_name = 'account'

urlpatterns = [
    path('api-token-register/', api_token_register, name='api-token-register'),
    path('api-token-auth/', obtain_auth_token, name='api-token-auth'),
    path('register/', register, name='register'),
    path('logout/', auth_views.logout, {'next_page': '/'}, name='logout'),
    path('login/', auth_views.login, {'template_name': 'accounts/login.html'}, name='login'),
]