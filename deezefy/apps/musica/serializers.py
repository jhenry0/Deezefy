from datetime import datetime
from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from .models import Musica, Curte, Playlist, Cria, Grava


class MusicaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Musica
        fields = "__all__"


class CurteSerializer(serializers.ModelSerializer):
    ouvinte = serializers.SerializerMethodField()


    def get_ouvinte(self, instance):
        return instance.ouvinte.user.email
        
    class Meta:
        model = Curte
        fields = "__all__"


class PlaylistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Playlist
        fields = "__all__"


class CriaSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    playlist = serializers.SerializerMethodField()

    def get_user(self, instance):
        return instance.user.email

    def get_playlist(self, instance):
        return instance.playlist.nome

    class Meta:
        model = Cria
        fields = "__all__"


class GravaSerializer(serializers.ModelSerializer):

    artista = serializers.SerializerMethodField()


    def get_artista(self, instance):
        return instance.artista.user.email

    class Meta:
        model = Grava
        fields = "__all__"