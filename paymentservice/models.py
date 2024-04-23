from django.db import models

from store.models import Customer, Product


# Create your models here.
class Order(models.Model):
    state_types = {"p": "pending", "o": "out for delivery", "d": "delivered"}

    payment_method = models.CharField(max_length=50)
    amount = models.IntegerField()
    state = models.CharField(choices=state_types)
    user = models.ForeignKey(to=Customer)

    # make a through table with quantity ???
    products = models.ManyToManyField(to=Product, through="OrderItems")

    def __str__(self):
        return self.user_id.name + "'s order ID " + self.id


class OrderItems(models.Model):
    order = models.ForeignKey(to=Order, on_delete=models.SET_NULL)
    product = models.ForeignKey(to=Product, on_delete=models.SET_NULL)
    quantity = models.IntegerField()
