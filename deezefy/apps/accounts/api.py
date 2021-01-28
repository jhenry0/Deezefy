from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import UserSerializer, OuvinteSerializer, ArtistaSerializer, SegueSerializer
from .models import User, Listener, Artist, Segue


class UserViewSet(viewsets.ModelViewSet):
    authentication_classes = []
    permission_classes = []
    serializer_class = UserSerializer
    queryset = User.objects.all()


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

class SegueViewSet(viewsets.ModelViewSet):
    authentication_classes = []
    permission_classes = []
    serializer_class = SegueSerializer
    queryset = Segue.objects.all()