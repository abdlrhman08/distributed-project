from datetime import datetime, timedelta, timezone

import jwt
from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework.authentication import BaseAuthentication, authenticate
from rest_framework.exceptions import AuthenticationFailed

User = get_user_model()

class JWToken:
    """
        Token wrapper class
    """

    def __init__(self, token=None):
        if token:
            try:
                self._token = jwt.decode(token, settings.SECRET_KEY, settings.ALGORITHM)
                self.encoded_token = token
            except jwt.DecodeError:
                # same exception for now
                raise

    def __getattr__(self, name):
        # try/catch is used to prevent recursion
        try:
            return self.__dict__[name]
        except KeyError:
            pass

        try:
            return self._token[name]
        except KeyError:
            raise

    def __str__(self):
        return self.encoded_token

    @classmethod
    def get_for_user(cls, username, password):
        user = authenticate(username=username, password=password)
        if not user:
            raise AuthenticationFailed
        
        cls_instance = cls()
        cls_instance._token = {
            "user_id": user.id,
            "exp": datetime.now(tz=timezone.utc) + timedelta(hours=24)
        }
        cls_instance.encoded_token = jwt.encode(cls_instance._token, settings.SECRET_KEY, settings.ALGORITHM)
        return cls_instance



class JWTAuthenticator(BaseAuthentication):
    def authenticate(self, request):
        token  = self._get_token(request)
        user = User.objects.get(id=token.user_id)
        
        return user, token
    def _get_token(self, request):
        token_header: str = request.headers.get("Authorization", None)
        if not token_header:
            raise AuthenticationFailed("Permission denied")

        try:
            token = token_header.split("Bearer")[1].lstrip()
            token = JWToken(token)
        except (IndexError, jwt.DecodeError):
            raise AuthenticationFailed("Permission denied")

        return token
