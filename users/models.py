from django.db import models
from django.contrib.auth.models import AbstractUser

class Rol(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'rol'
        

class User(AbstractUser):
    rol = models.ForeignKey(Rol,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=50,null=True,blank=True)
    tel = models.CharField(max_length=20, null=True, blank=True)
    image = models.ImageField(upload_to='avatars/',null=True,blank=True)
    author = models.ForeignKey('users.User',on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.username
    

    class Meta:
        db_table = 'user'


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    name = models.TextField()
    date = models.DateField(auto_now_add=True,null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'comment'