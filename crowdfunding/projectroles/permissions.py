from rest_framework import permissions

class IsCreatorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:#just get and options preloaded in permissions library
            return True
        return obj.creator == request.user