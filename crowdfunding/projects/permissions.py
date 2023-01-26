from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:#just get and options preloaded in permissions library
            return True
        return obj.owner == request.user

class IsSupporterOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:#just get and options preloaded in permissions library
            return True
        return obj.supporter == request.user

    #This is a custom permision