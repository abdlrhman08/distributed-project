from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.views import APIView, Response

from .authenticator import JWToken
from .mixins import RestrictedViewMixin
from .serializers import CredientalsSerializer


class AuthenticateUserView(APIView):
    def post(self, request, format=None):
        user_credientals = CredientalsSerializer(data=request.data)
        if user_credientals.is_valid():
            username = user_credientals.validated_data["username"]
            password = user_credientals.validated_data["password"]
            
            access_token = JWToken.get_for_user(username, password)
            
            return Response({ "token": str(access_token) })

        return Response({ "details": "Invalid form"}, status=HTTP_400_BAD_REQUEST)

class RegisterUserView(APIView):
    def post(self, request):
        pass

class DummyView(RestrictedViewMixin, APIView):
    def get(self, request):
        content = {
            "user": str(request.user)
        }

        return Response(content)
