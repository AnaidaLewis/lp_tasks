from django import forms
from .models import ToDoList

class List(forms.ModelForm):
	class Meta:
		model = ToDoList
		fields = '__all__'
