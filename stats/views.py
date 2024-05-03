from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from authentication.authenticator import JWTAuthenticator
from store.serializers import ProductSerlializer

from .models import Customer, Seller
from .serializers import SellerSerializer, WishlistProductSerializer


class SellerListView(generics.ListAPIView):
    serializer_class = SellerSerializer

    def get_queryset(self):
        number = int(self.request.query_params.get("n", 10))
        queryset = Seller.objects.all()[:number]
        return queryset


class AddProductToWishlistView(APIView):
    serializer_class = WishlistProductSerializer
    authentication_classes = [JWTAuthenticator]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK)


class RemoveProductWishlistView(generics.DestroyAPIView):
    authentication_classes = [JWTAuthenticator]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        self.customer = self.request.user.customer
        self.wishlist = self.customer.wishlist
        return self.wishlist

    def perform_destroy(self, instance):
        self.wishlist.remove(instance)

  
class ClearWishlistView(generics.DestroyAPIView):
    authentication_classes = [JWTAuthenticator]
    permission_classes = [IsAuthenticated]

    def get_object(self):
        customer = self.request.user.customer
        return customer.wishlist

    def perform_destroy(self, instance):
        # instance here is the wishlist
        instance.clear()


class GetWishlistView(generics.ListAPIView):
    serializer_class = ProductSerlializer
    authentication_classes = [JWTAuthenticator]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        customer = Customer.objects.get(user=user)
        return customer.wishlist
