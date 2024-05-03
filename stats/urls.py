from django.urls import path

from .views import (
    AddProductToWishlistView,
    ClearWishlistView,
    GetWishlistView,
    RemoveProductWishlistView,
    SellerListView,
)

urlpatterns = [
    path("sellers/", SellerListView.as_view()),
    path('add-product/', AddProductToWishlistView.as_view()),
    path('remove-product/<int:pk>/', RemoveProductWishlistView.as_view()),
    path('clear-wishlist/', ClearWishlistView.as_view()),
    path('get-wishlist/', GetWishlistView.as_view(), name='get_wishlist')
]

