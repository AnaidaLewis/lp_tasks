from django import forms
from .models import MyUser
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, UserChangeForm 



class RegisterForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ["username","first_name","last_name","email","password1","password2"]


