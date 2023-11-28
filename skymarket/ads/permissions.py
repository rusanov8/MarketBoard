from rest_framework.permissions import BasePermission


class IsAdminOrOwner(BasePermission):
    """
       Custom permission class to allow access to admin or the owner of the object.
    """

    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            if request.user.is_admin:
                return True
            return obj.author == request.user
        return False

