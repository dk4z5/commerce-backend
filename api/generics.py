from rest_framework import generics

class PermHook():
    def get_permissions(self):
        try:
            # return permission_classes depending on `action` 
            return [permission() for permission in self.permission_classes_by_action[self.request.method]]
        except (KeyError, AttributeError): 
            # action is not set return default permission_classes
            return [permission() for permission in self.permission_classes]

class ListCreateAPIView(generics.ListCreateAPIView, PermHook):
    def get_permissions(self):
        return PermHook.get_permissions(self)

class RetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView, PermHook):
    def get_permissions(self):
        return PermHook.get_permissions(self)

class ListAPIView(generics.ListAPIView, PermHook):
    def get_permissions(self):
        return PermHook.get_permissions(self)

class UpdateAPIView(generics.UpdateAPIView, PermHook):
    def get_permissions(self):
        return PermHook.get_permissions(self)