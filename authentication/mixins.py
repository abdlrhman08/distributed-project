class RestrictedViewMixin:
    """
        Use this mixin to verify a JWT token is sent in the header.
    """
    authentication_classes = []
