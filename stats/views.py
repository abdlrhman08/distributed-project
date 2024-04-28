from rest_framework import status
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from authentication.authenticator import JWTAuthenticator
from stats.serializers import (
    CartItemListCreateSerializer,
    CartItemUpdateDeleteSerializer,
)

from .models import CartItem


class CartItemListView(ListCreateAPIView):
    serializer_class = CartItemListCreateSerializer
    authentication_classes = [JWTAuthenticator]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        customer = self.request.user
        items = CartItem.objects.filter(customer__user=customer)
        return items


# Make it update / delete only
class CartItemDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = CartItemUpdateDeleteSerializer
    queryset = CartItem.objects.all()
    authentication_classes = [JWTAuthenticator]
    permission_classes = [IsAuthenticated]


class CartDeleteView(APIView):
    authentication_classes = [JWTAuthenticator]
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        customer = self.request.user.customer
        if customer:
            cart_items = CartItem.objects.filter(customer=customer)
            cart_items.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)
