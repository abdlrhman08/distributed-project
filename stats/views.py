from rest_framework import generics
from .models import Seller,Customer
from .serializers import SellerSerializer
from django.http import JsonResponse
from django.views.generic import View
class SellerListView(generics.ListAPIView):
    serializer_class = SellerSerializer

    def get_queryset(self):
        number = int(self.request.query_params.get("n", 10))
        queryset = Seller.objects.all()[:number]
        return queryset

class AddProductToWishlistView(View):

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = request.POST
        customer_name = data.get('customer_name')
        product_name = data.get('product_name')
        if not customer_name or not product_name:
            return JsonResponse({"error": "Customer name and product name are required"}, status=400)
        response = Customer.wishlist.add_product(customer_name, product_name)
        return JsonResponse(response)

class RemoveProductFromWishlistView(View):

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = request.POST
        customer_name = data.get('customer_name')
        product_name = data.get('product_name')
        if not customer_name or not product_name:
            return JsonResponse({"error": "Customer name and product name are required"}, status=400)
        response = Customer.wishlist.remove_product(customer_name, product_name)
        return JsonResponse(response)

class RemoveAllProductsFromWishlistView(View):

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = request.POST
        customer_name = data.get('customer_name')
        if not customer_name:
            return JsonResponse({"error": "Customer name is required"}, status=400)
        response = Customer.wishlist.remove_all_products(customer_name)
        return JsonResponse(response)

class GetWishlistView(View):

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        customer_name = request.GET.get('customer_name')
        if not customer_name:
            return JsonResponse({"error": "Customer name is required"}, status=400)
        wishlist = Customer.wishlist.get_wishlist(customer_name)
        return JsonResponse({"wishlist": list(wishlist)})
