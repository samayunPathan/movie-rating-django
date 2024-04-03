from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin

from .manager import UserManager

# Create your models here.

class User(AbstractBaseUser,PermissionsMixin):
    username = models.CharField(max_length=150, unique=True,null=True)
    email=models.EmailField(unique=True)
    phone=models.CharField(max_length=14,blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects=UserManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username']

    def __str__(self):
        return self.email
