from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import MusicaSerializer, CurteSerializer, PlaylistSerializer, CriaSerializer, GravaSerializer
from .models import Musica, Curte, Playlist, Cria, Grava


class MusicaViewSet(viewsets.ModelViewSet):
    authentication_classes = []
    permission_classes = []
    serializer_class = MusicaSerializer
    queryset = Musica.objects.all()


class CurteViewSet(viewsets.ModelViewSet):
    authentication_classes = []
    permission_classes = []
    serializer_class = CurteSerializer
    queryset = Curte.objects.all()


class PlaylistViewSet(viewsets.ModelViewSet):
    authentication_classes = []
    permission_classes = []
    serializer_class = PlaylistSerializer
    queryset = Playlist.objects.all()


class CriaViewSet(viewsets.ModelViewSet):
    authentication_classes = []
    permission_classes = []
    serializer_class = CriaSerializer
    queryset = Cria.objects.all()


class GravaViewSet(viewsets.ModelViewSet):
    authentication_classes = []
    permission_classes = []
    serializer_class = GravaSerializer
    queryset = Grava.objects.all() 