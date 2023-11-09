from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Rol(models.Model):
    nomi = models.CharField(max_length=50)

    def __str__(self):
        return self.nomi

class User(AbstractUser):
    rol = models.ForeignKey(Rol,on_delete=models.CASCADE,null=True,blank=True)
    nomi = models.CharField(max_length=50,null=True,blank=True)
    image = models.ImageField(upload_to='avatars/', default='avatars/default.jpg',null=True,blank=True)
    author = models.ForeignKey('users.User',on_delete=models.CASCADE, null=True, blank=True)
    parol = models.CharField(max_length=50,null=True,blank=True)

    def __str__(self):
        return self.username
