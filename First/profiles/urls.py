from django.contrib import admin
from django.urls import path
from profiles.views import ConfirmEmail,Login,Logout,CreateUser,ProfileCreateView,ProfileUpdateView
app_name="profiles"
urlpatterns = [
    path("create/",ProfileCreateView.as_view(),name="create_profile"),
    path("update/<int:lo>",ProfileUpdateView.as_view(),name="update_profile"),
    path("signup/",CreateUser,name="create_user"),
    path("logout/",Logout,name="logout_user"),
    path("login/",Login,name="login_user"),
    path("confirm_email/",ConfirmEmail.as_view(),name="confirm_email"),
]
