from django.contrib.auth.forms import (
    UserCreationForm, 
)
from django import forms
from django.contrib.auth.models import User
from .models import Profile


class RegForm(UserCreationForm):
    email = forms.EmailField(label='Email', max_length=100)
    first_name = forms.CharField(max_length=70)
    last_name = forms.CharField(max_length=70)
    nationality = forms.CharField(max_length=15)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'nationality', 'password1', 'password2')


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(label='Enter Your Email')

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
