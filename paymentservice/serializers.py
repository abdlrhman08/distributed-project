
from datetime import datetime

from rest_framework import serializers

from paymentservice.models import PaymentDetails
from stats.models import CartItem
from store.serializers import ProductSerializer

from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ["payment_method", "amount", "state", "customer", "products"]
        read_only_fields = ["amount", "state", "customer", "products"]

    def create(self, validated_data):
        customer = self.context["customer"]
        user_cart = CartItem.objects.filter(customer=customer).select_related("product")
        order = Order.objects.create(**validated_data, customer=customer, amount=0)

        # this whole operation could be optimized
        amount = 0
        for cart_item in user_cart:
            referred_product = cart_item.product
            product_seller = referred_product.seller

            referred_product.quantity -= cart_item.quantity
            referred_product.total_sold += cart_item.quantity
            product_seller.total_products_sold += cart_item.quantity
            product_seller.total_revenue += referred_product.price
            amount += referred_product.price

            order.products.add(
                referred_product, through_defaults={"quantity": cart_item.quantity}
            )

            # the two saves here could be optimized by appending the different
            # sellers to a set and the different products and saving them invidually
            product_seller.save()
            referred_product.save()
        order.amount = amount
        order.save()

        return order


class PaymentDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentDetails
        fields = "__all__"
        read_only_fields = ["id"]

    def validate(self, attrs):
        if attrs["payment_method"] not in ["credit card", "cash"]:
            raise serializers.ValidationError("Invalid payment method")

        if attrs["payment_method"] == "credit card":
            if len(attrs["credit_card_number"]) != 16:
                raise serializers.ValidationError("Invalid credit card number")

            if len(attrs["payment_amount"]) < 0:
                raise serializers.ValidationError("Invalid payment amount")

            if attrs["payment_date"] > datetime.now():
                raise serializers.ValidationError("Invalid payment date")

            if attrs["credit_card_expiry"] < datetime.now():
                raise serializers.ValidationError("Invalid credit card expiry date")

        if attrs["payment_method"] == "cash":
            if len(attrs["payment_amount"]) < 0:
                raise serializers.ValidationError("Invalid payment amount")

            if attrs["payment_date"] > datetime.now():
                raise serializers.ValidationError("Invalid payment date")

        return True
