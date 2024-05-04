from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from authentication.authenticator import JWTAuthenticator

from .models import Order
from .serializers import OrderSerializer, PaymentDetailsSerializer


class ViewPerformOrdersView(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    authentication_classes = [JWTAuthenticator]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        customer = self.request.user.customer
        return Order.objects.filter(customer=customer)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["customer"] = self.request.user.customer
        return context


class OrderDetailView(generics.RetrieveAPIView):
    serializer_class = OrderSerializer
    authentication_classes = [JWTAuthenticator]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        customer = self.request.user.customer
        return Order.objects.filter(customer=customer)


class CreatePaymentView(APIView):
    serializer_class = PaymentDetailsSerializer
    authentication_classes = [JWTAuthenticator]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = PaymentDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"payment_created": True}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
