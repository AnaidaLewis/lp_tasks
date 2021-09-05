from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class MyUser(AbstractUser):
    profile_picture = models.ImageField(null = True, blank= True)
    email = models.EmailField(unique=True, blank = False)