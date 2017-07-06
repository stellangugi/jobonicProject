from rest_framework import permissions


class UpdateBasicProfile(permissions.BasePermission):
    """Allows users to edit their basic profile"""

    def has_object_permission(self, request, view, obj):
        """Check if user is trying to edit their own profile"""

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id


class PostOwnProfile(permissions.BasePermission):
    """Allow users to update their profile."""

    def has_object_permission(self, request, view, obj):
        """Checks if the user is trying to edit their main profile"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user.id == request.user.id