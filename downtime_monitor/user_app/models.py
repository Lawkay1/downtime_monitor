from django.db import models
from django.contrib.auth.models import AbstractUser
from user_app.manager import CustomUserManager


# Create your models here.
'''
details needed include 
firstname, lastname, email
'''

class User(AbstractUser):
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=80, unique=True)
 
    USERNAME_FIELD= 'email'
    REQUIRED_FIELDS=    ['username']
    
    objects=CustomUserManager()
    
    def __str__(self):
        return f"<User {self.email}"