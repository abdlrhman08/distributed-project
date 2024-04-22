from django.urls import path

from .views import AuthenticateUserView, DummyView

urlpatterns = [
    path("login/", AuthenticateUserView.as_view()),
    path("auth-test/", DummyView.as_view())
]
