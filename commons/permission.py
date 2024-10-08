from rest_framework.permissions import BasePermission


class IsSuperUser(BasePermission):
 def has_permission(self, request, view):
  return request.user and request.user.is_superuser
 


class IsAdmin(BasePermission):
 def has_permission(self, request, view):
  return request.user and ('admin' == request.user.role)
 

class IsSelfOrReadOnly(BasePermission):
 
 def has_object_permission(self, request, view, obj):
  print(obj)
  print(request)
  print(request.user)
  return obj == request.user


