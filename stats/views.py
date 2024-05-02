from rest_framework import generics
from .models import Seller,Customer
from .serializers import SellerSerializer,CustomerSerializer
from django.http import JsonResponse
from django.views.generic import View
from rest_framework.response import Response
class SellerListView(generics.ListAPIView):
    serializer_class = SellerSerializer

    def get_queryset(self):
        number = int(self.request.query_params.get("n", 10))
        queryset = Seller.objects.all()[:number]
        return queryset

class AddProductToWishlistView(generics.CreateAPIView):
    serializer_class = CustomerSerializer

    def post(self, request, *args, **kwargs):
        user = self.request.user
        product = self.request.data.get('product')

        # Retrieve the customer based on the request user
        customer = Customer.objects.get(user=user)

        # Add the product to the wishlist
        customer.wishlist.add(product)


class RemoveProductWishlistView(generics.DestroyAPIView):
    serializer_class = CustomerSerializer

    def delete(self, request, *args, **kwargs):
        user = self.request.user
        product = self.request.data.get('product')

        # Retrieve the customer based on the request user
        customer = Customer.objects.get(user=user)

        # Remove the product from the wishlist
        customer.wishlist.remove(product)
class RemoveAllProducts_Wl_View(generics.DestroyAPIView):
    serializer_class = CustomerSerializer

    def delete(self, request, *args, **kwargs):
        user = self.request.user

        # Retrieve the customer based on the request user
        customer = Customer.objects.get(user=user)

        # Remove the product from the wishlist
        customer.wishlist.clear()

class GetWishlistView(generics.ListAPIView):
    serializer_class = CustomerSerializer

    def get_queryset(self):
        user = self.request
        if user:
            customer = Customer.objects.filter(user=user)
            return customer.wishlist
        return Customer.objects.none()

