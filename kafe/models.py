from django.db import models
from users.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    status = models.BooleanField(default=True)
    date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'category'
        

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    title = models.TextField(blank=True,null=True)
    summa = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='product')
    status = models.BooleanField(default=True)
    date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'product'


class Table(models.Model):
    name = models.CharField(max_length=50)
    status = models.BooleanField(default=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.name

    
    class Meta:
        db_table = 'table'