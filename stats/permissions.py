from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsCustomerAndAuthenticated(BasePermission):
    def has_permission(self, request, view):
        return bool(
            (
                request.user.is_authenticated
                and request.user.has_perm("stats.manage_cartitem")
            )
        )
