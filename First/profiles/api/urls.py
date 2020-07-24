from django.urls import path,include
from profiles.api.views import register_user,create_profile,send_otp,update_address
from rest_framework.authtoken.views import obtain_auth_token

app_name='profiles'

urlpatterns = [
	path('register_user/',register_user,name='register_user'),
	path('login_user/',obtain_auth_token,name='login_user'),
	path('create_profile/',create_profile,name='create_profile'),
	path('send_otp/',send_otp,name='send_otp'),
	path('update_address/',update_address,name='update_address')
]