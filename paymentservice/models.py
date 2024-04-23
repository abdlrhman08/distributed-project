from django.db import models


# Create your models here.
class Order(models.Model):
    state_types = {"p": "pending", "o": "out for delivery", "d": "delivered"}

    payment_method = models.CharField(max_length=50)
    amount = models.IntegerField()
    state = models.CharField(choices=state_types, max_length=1)
    user = models.ForeignKey("stats.customer", on_delete=models.DO_NOTHING)

    # make a through table with quantity ???
    products = models.ManyToManyField(to="store.product", through="OrderItems")

    def __str__(self):
        return self.user_id.name + "'s order ID " + self.id


class OrderItems(models.Model):
    order = models.ForeignKey(to=Order, on_delete=models.DO_NOTHING)
    product = models.ForeignKey("store.product", on_delete=models.DO_NOTHING)
    quantity = models.IntegerField()
