from django.db import models
from users.models import User
from kafe.models import *
# Create your models here.


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,null=True)
    table = models.ForeignKey(Table, on_delete=models.CASCADE, null=True)
    number = models.PositiveIntegerField()
    date_creat = models.DateField(auto_now_add=True)
    date_edit = models.DateField(auto_now=True)
    status = models.BooleanField(default=False)
    deliver = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    summa_all = models.PositiveIntegerField(default=0)
    
    def sum(self):
        return self.product.number * self.number
    
    class Meta:
        db_table = 'order'

