from django import forms
from .models import ToDoList
from register.models import  MyUser

class List(forms.ModelForm):
	class Meta:
		model = ToDoList
		fields = '__all__'
		exclude = ['user']

class Account(forms.ModelForm):
	class Meta:
		model = MyUser
		fields = ['first_name','last_name','email','profile_picture']
