from django.db import models
from django.db.models.deletion import CASCADE
from django.utils import timezone as tz
from register.models import MyUser

# Create your models here.

class ToDoList(models.Model):
    user = models.OneToOneField(MyUser, null = True, on_delete = CASCADE)
    name = models.CharField(max_length=200)
    Created = models.DateTimeField(null = True, blank = False, auto_now_add = True)
    
    def __str__(self):
        return self.name

class Item(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    complete = models.BooleanField()

    def __str__(self):
        return self.text

