from django.db import models
from users.models import User
from kafe.models import *
# Create your models here.

class Zakas(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,null=True)
    stol = models.ForeignKey(Stol, on_delete=models.CASCADE, null=True)
    soni = models.PositiveIntegerField(default=0,null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    buyurtma = models.BooleanField(default=False)

    def sum(self):
        return self.product.narxi * self.soni

