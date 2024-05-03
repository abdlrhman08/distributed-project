from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from stats.views import (
    CartDeleteView,
    CartItemDetailView,
    CartItemListView,
    SellerListView,
)

urlpatterns = [
    path("sellers/", SellerListView.as_view()),
    path("cart/", CartDeleteView.as_view()),
    path("cart-items/", CartItemListView.as_view()),
    path("cart-items/<int:pk>", CartItemDetailView.as_view()),
]
