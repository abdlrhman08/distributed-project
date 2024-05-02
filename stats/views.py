from rest_framework import generics, status
from rest_framework.views import APIView

from .models import Seller,Customer
from .serializers import SellerSerializer,CustomerSerializer
from django.views.generic import View
from rest_framework.response import Response
from authentication.authenticator import JWTAuthenticator
from rest_framework.permissions import IsAuthenticated
class SellerListView(generics.ListAPIView):
    serializer_class = SellerSerializer

    def get_queryset(self):
        number = int(self.request.query_params.get("n", 10))
        queryset = Seller.objects.all()[:number]
        return queryset

class AddProductToWishlistView(APIView):
    serializer_class = CustomerSerializer
    authentication_classes = [JWTAuthenticator]
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        user = self.request.user
        product = self.request.data.get('product')

        # Retrieve the customer based on the request user
        customer = Customer.objects.get(user=user)

        # Add the product to the wishlist
        customer.wishlist.add(product)

        return Response({"details": "Product added to wishlist"},status= status.HTTP_201_CREATED)

class RemoveProductWishlistView(generics.DestroyAPIView):
    serializer_class = CustomerSerializer
    authentication_classes = [JWTAuthenticator]
    permission_classes = [IsAuthenticated]
    def delete(self, request, *args, **kwargs):
        user = self.request.user
        product = self.request.data.get('product')

        # Retrieve the customer based on the request user
        customer = Customer.objects.get(user=user)

        # Remove the product from the wishlist
        customer.wishlist.remove(product)

        return Response({"details": "Product removed from wishlist"})
class ClearWishlistView(generics.DestroyAPIView):
    serializer_class = CustomerSerializer
    authentication_classes = [JWTAuthenticator]
    permission_classes = [IsAuthenticated]
    def delete(self, request, *args, **kwargs):
        user = self.request.user

        # Retrieve the customer based on the request user
        customer = Customer.objects.get(user=user)

        # Remove the product from the wishlist
        customer.wishlist.clear()

        return Response({"details": "Wishlist cleared"})
class GetWishlistView(generics.ListAPIView):
    serializer_class = CustomerSerializer
    authentication_classes = [JWTAuthenticator]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user:
            customer = Customer.objects.filter(user=user)
            return customer.wishlist
        return Customer.objects.none()

