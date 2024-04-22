from django.contrib import auth
from rest_framework_simplejwt.authentication import JWTAuthentication


class RestrictedViewMixin:
    """
        Use this mixin to verify a JWT token is sent in the header.
        If dispatch() is overriden in the view, super().dispatch must be called
        in the start of the method. Must be before APIView in the MRO
    """

    def dispatch(self, request, *args, **kwargs):
        authenticator = JWTAuthentication()
        try:
            user, token = authenticator.authenticate(request)
            request.user = user   
        except Exception:
            pass

        super().dispatch(request, *args, **kwargs)
