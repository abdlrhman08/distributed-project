from rest_framework import status
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.response import Response
from rest_framework.views import APIView

from stats.serializers import (
    CartItemListCreateSerializer,
    CartItemUpdateDeleteSerializer,
)

from .models import CartItem


class CartItemListView(ListCreateAPIView):
    serializer_class = CartItemListCreateSerializer

    def get_queryset(self):
        customer = self.request.query_params.get("customer")
        items = CartItem.objects.filter(customer=customer)
        return items


# Make it update / delete only
class CartItemDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = CartItemUpdateDeleteSerializer
    queryset = CartItem.objects.all()


class CartDeleteView(APIView):
    def delete(self, request, *args, **kwargs):
        customer = self.request.data.get("customer")
        if customer:
            cart_items = CartItem.objects.filter(customer=customer)
            cart_items.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)
