from django.contrib.auth import authenticate
from rest_framework.views import APIView, Response

from .mixins import RestrictedViewMixin
from .serializers import CredientalsSerializer
from .utils import get_token_for_user


# TODO: figure oute a better name 
class AuthenticateUserView(APIView):
    def post(self, request, format=None):
        user_credientals = CredientalsSerializer(data=request.data)
        if user_credientals.is_valid():
            username = user_credientals.validated_data["username"]
            password = user_credientals.validated_data["password"]
            user = authenticate(username=username, password=password)    
            access_tokens = get_token_for_user(user)
            return Response(access_tokens)

        return Response("Invalid Credientals")

class RegisterUserView(APIView):
    pass

class DummyView(RestrictedViewMixin, APIView):
    def post(self, request):
        return Response("Hello this is a restricted view")
