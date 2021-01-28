from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import UserSerializer, OuvinteSerializer, ArtistaSerializer
from .models import User, Listener, Artist



class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        obj = queryset.get(pk=self.request.user.id)
        self.check_object_permissions(self.request, obj)
        return obj

    def get_permissions(self):
        return [] if self.action in ("create", "login") else [IsAuthenticated()]

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def list(self, request):
        user = self.get_queryset().first()
        serializer = self.serializer_class(user)
        return Response(serializer.data)

class OuvinteViewSet(viewsets.ModelViewSet):
    authentication_classes = []
    permission_classes = []
    serializer_class = OuvinteSerializer
    queryset = Listener.objects.all()

class ArtistaViewSet(viewsets.ModelViewSet):
    authentication_classes = []
    permission_classes = []
    serializer_class = ArtistaSerializer
    queryset = Artist.objects.all()