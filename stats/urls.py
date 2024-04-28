from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from stats.views import CartDeleteView, CartItemDetailView, CartItemListView

# from .views import CategoryList, CategoryView, ProductList, ProductView

urlpatterns = [
    path("cart/", CartDeleteView.as_view()),
    path("cart-items/", CartItemListView.as_view()),
    path("cart-items/<int:pk>", CartItemDetailView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
