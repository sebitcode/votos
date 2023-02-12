from rest_framework import permissions

class BlockLeaderPermission(permissions.BasePermission):
    """
    Global permission check for blocked IPs.
    """

    def has_permission(self, request, view):
        user = request.user
        return user.username.split("_")[-1] != "leader"

class BlockLeaderAutoCreatePermission(permissions.BasePermission):
    """
    Global permission check for blocked IPs.
    """

    def has_permission(self, request, view):
        user = request.user
        return not (user.username.split("_")[-1] == "leader" and request.method in ["POST", "post"])

class BlockLeaderAutoUpdateDeletePermission(permissions.BasePermission):
    """
    Global permission check for blocked IPs.
    """

    def has_permission(self, request, view):
        user = request.user
        return not (user.username.split("_")[-1] == "leader" and request.method in ["PUT", "put", "DELETE", "delete"])
