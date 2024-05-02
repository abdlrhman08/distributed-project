from django.urls import path

from .views import SellerListView
from . import views
urlpatterns = [path("sellers/", SellerListView.as_view()),
               path('add-product/', views.AddProductToWishlistView.as_view()),
               path('remove-product/', views.RemoveProductFromWishlistView.as_view()),
               path('remove-all-products/', views.RemoveAllProductsFromWishlistView.as_view()),
               path('get-wishlist/', views.GetWishlistView.as_view(), name='get_wishlist')
               ]
