from django import forms
from .models import MyUser
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, UserChangeForm 



class RegisterForm(UserCreationForm):
    # the hashed code below is used to customise the field say u want the last name to be max 5 letters so u can overide that with this..but if u want it to be normal u just need to add the required fields in meta
    # first_name = forms.CharField(max_length = 100)
    # last_name = forms.CharField(max_length = 100)
    # email = forms.EmailField()
    class Meta:
        model = MyUser
        fields = ["username","first_name","last_name","email","password1","password2","profile_picture"]


