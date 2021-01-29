from datetime import datetime
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer

from .models import Musica, Curte, Playlist, Cria, Grava
from apps.accounts.models import Listener, Artist, User

class MusicaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Musica
        fields = "__all__"


class CurteSerializer(serializers.ModelSerializer):
    ouvinte = serializers.SerializerMethodField()
    ouvinte_email = serializers.EmailField(write_only=True)

    def create(self, validated_data):
        ouvinte = Listener.objects.get(user__email=validated_data["ouvinte_email"])
        instance = Curte.objects.create(
            musica=validated_data["musica"],
            ouvinte=ouvinte
            ) 
        return instance

    def update(self, instance, validated_data):
        ouvinte = Listener.objects.get(user__email=validated_data["ouvinte_email"])
        Curte.objects.filter(id=instance.id).update(
            musica=validated_data["musica"],
            ouvinte=ouvinte
            ) 

        return Curte.objects.filter(id=instance.id).first()

    def get_ouvinte(self, instance):
        return instance.ouvinte.user.email
        
    class Meta:
        model = Curte
        fields = "__all__"


class PlaylistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Playlist
        fields = "__all__"


class CriaSerializer(WritableNestedModelSerializer):
    user = serializers.SerializerMethodField()
    user_email = serializers.EmailField(write_only=True)
    playlist = PlaylistSerializer()

    def create(self, validated_data):
        user = User.objects.get(email=validated_data["user_email"])
        playlist = Playlist.objects.create(**validated_data["playlist"])
        instance = Cria.objects.create(
            user=user,
            playlist=playlist,
            ) 
        return instance

    def update(self, instance, validated_data):
        user = User.objects.get(email=validated_data["user_email"])
        instance.playlist = Playlist(**validated_data["playlist"])
        instance.playlist.save()
        Cria.objects.filter(id=instance.id).update(
            user=user,
            ) 

        return Cria.objects.filter(id=instance.id).first()

    def get_user(self, instance):
        return instance.user.email

    def get_playlist(self, instance):
        return instance.playlist.nome

    class Meta:
        model = Cria
        fields = "__all__"


class GravaSerializer(serializers.ModelSerializer):
    artista = serializers.SerializerMethodField()
    artista_email = serializers.EmailField(write_only=True)

    def create(self, validated_data):
        artista = Artist.objects.get(user__email=validated_data["artista_email"])
        instance = Grava.objects.create(
            musica=validated_data["musica"],
            artista=artista
            ) 
        return instance

    def update(self, instance, validated_data):
        artista = Artist.objects.get(user__email=validated_data["artista_email"])
        Grava.objects.filter(id=instance.id).update(
            musica=validated_data["musica"],
            artista=artista
            ) 

        return Grava.objects.filter(id=instance.id).first()


    def get_artista(self, instance):
        return instance.artista.user.email

    class Meta:
        model = Grava
        fields = "__all__"