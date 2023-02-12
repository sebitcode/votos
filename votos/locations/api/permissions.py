from rest_framework import permissions

class BlockLeaderPermission(permissions.BasePermission):
    """
    Global permission check for blocked IPs.
    """

    def has_permission(self, request, view):
        user = request.user
        return not (user.username.split("_")[-1] == "leader" and request.method in ["PUT", "put", "DELETE", "delete", "POST", "post"])
