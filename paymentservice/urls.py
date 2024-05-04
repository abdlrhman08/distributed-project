from django.urls import path

from .views import CreatePaymentView, OrderDetailView, ViewPerformOrdersView

urlpatterns = [
    path('check-payment', CreatePaymentView.as_view()),
    path("order/", ViewPerformOrdersView.as_view()),
    path("order/<int:pk>/", OrderDetailView.as_view()),
]
