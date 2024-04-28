from rest_framework.schemas.coreapi import serializers

from .models import CartItem


class CartItemListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ["id", "customer", "product", "quantity"]
        read_only_fields = ["id", "customer"]

    def create(self, validated_data):
        validated_data["customer"] = self.context["request"].user.customer
        obj = CartItem.objects.create(**validated_data)
        return obj


class CartItemUpdateDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ["id", "customer", "product", "quantity"]
        read_only_fields = ["id", "customer", "product"]
