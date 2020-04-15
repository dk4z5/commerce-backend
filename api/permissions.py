from rest_framework import permissions

class AuthAndEmployer(permissions.BasePermission):

    def has_permission(self, request, view):
        
        if request.method not in permissions.SAFE_METHODS:
            return False
        
        if request.user == None:
            return False
        
        
        for group in request.user.groups.all():
            if group.name == 'empregados':
                return True
        return False
