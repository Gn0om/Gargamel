from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['image']

class ProfileUpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        friends = ['image']

class UserDeleteForm(forms.ModelForm):
    class Meta:
        model = User
        friends = []
    