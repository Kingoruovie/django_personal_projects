from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
	profile_pic = forms.ImageField(required=False)

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2', 'profile_pic']