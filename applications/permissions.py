from rest_framework.permissions import BasePermission

class ApplicationPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ("GET", "HEAD", "OPTIONS"):
            return obj.candidate == request.user or obj.job.created_by == request.user
        return obj.candidate == request.user
