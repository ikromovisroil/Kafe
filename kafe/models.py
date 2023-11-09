from django.db import models
from users.models import User
# Create your models here.
class Category(models.Model):
    nomi = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.nomi


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True)
    nomi = models.CharField(max_length=50)
    izox = models.TextField(blank=True,null=True)
    narxi = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='product')
    author = models.ForeignKey(User, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.nomi


class Stol(models.Model):
    nomi = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.nomi


