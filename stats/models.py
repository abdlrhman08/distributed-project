from django.contrib.auth import get_user_model
from django.db import models

from stats import views
from store.models import Product

User = get_user_model()


# Create your models here.
class Customer(models.Model):
    user_id = models.OneToOneField(to=User, primary_key=True)
    address = models.CharField(max_length=150)
    wishlist = models.ManyToManyField(to=Product)

    def __str__(self):
        return "Customer: " + self.name


class Seller(models.Model):
    user = models.OneToOneField(to=User, primary_key=True)
    company_name = models.CharField(max_length=50)
    location = models.CharField(max_length=150)

    def __str__(self):
        return "Seller: " + self.company_name


class CartItem(models.Model):
    user = models.ForeignKey(to=Customer, on_delete=models.CASCADE)
    cart_item = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return self.name + "'s cart"


class Stats(models.Model):
    product_id = models.OneToOneField(to=Product, primary_key=True)
    views = models.IntegerField()
    rating = models.IntegerField()
    likes = models.IntegerField()
    dislikes = models.IntegerField()

    def __str__(self):
        return self.name + "'s view = " + views


class Comment(models.Model):
    stats = models.ForeignKey(to=Stats, on_delete=models.CASCADE)
    author = models.ForeignKey(to=User, on_delete=models.SET_NULL)
    comment = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
