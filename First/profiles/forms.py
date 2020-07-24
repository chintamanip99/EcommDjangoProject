from django import forms
from .models import Profiles
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class ProfileModelForm(forms.ModelForm):
	class Meta:
		model=Profiles
		fields=[
		'balance',
		'age',
		]

class UserCreateForm(UserCreationForm):
	class Meta:
		model=User
		fields=[
			'username',
			'email',
			'password1',
			'password2'
		]

class ConfirmEmailForm(forms.Form):
	otp=forms.CharField(widget=forms.TextInput(attrs={"placeholder":"OTP"}))

class RawLoginForm(forms.Form):
	username=forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Username"}))
	password=forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Password"}))
	