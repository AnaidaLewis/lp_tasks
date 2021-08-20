from django import forms
from .models import ToDoList, Item

class List(forms.ModelForm):
	class Meta:
		model = ToDoList
		fields = '__all__'

class Items(forms.ModelForm):
	class Meta:
		model = Item
		fields = '__all__'