from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm, UserChangeForm, UserCreationForm
from django.db import models
from django.db.models.fields import files
from django.forms import fields, widgets
from django import forms

class RegistrationForm(UserCreationForm):
    username = forms.CharField(
        label='Enter username/email',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'example@gmail.com'})
    )
    password1 = forms.CharField(
        label='Enter Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Enter Password'})
    )
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Enter Again'})
    )
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
