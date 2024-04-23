from django.db import models

from stats.models import Seller


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    price = models.IntegerField()
    quantity = models.IntegerField()
    category = models.ForeignKey(Category, on_delete= models.SET_NULL)
    seller = models.ForeignKey(to=Seller, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
