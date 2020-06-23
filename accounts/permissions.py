from rest_framework import permissions

SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')

class IsAdminUserOrAuthenticatedOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        elif request.method == 'POST':
            return request.user and request.user.is_authenticated
        else:
            return request.user and request.user.is_staff #(is_admin?)

    #def has_object_permission(self, request, view, obj):
        #return request.user and request.user.is_superuser