from datetime import datetime
from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from .models import User, Listener, Artist, Segue


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    username = serializers.CharField(required=False)
    age = serializers.SerializerMethodField()

    def get_age(self, instance):
        return datetime.now().year - instance.birthday.year
        
    def validate(self, data):
        if "password" in data:
            data["password"] = make_password(data["password"])
        if "email" in data:
            data["username"] = data["email"]
        
        return data

    class Meta:
        model = User
        fields = ["id", "username", "password", "birthday", "email", "age"] 


class OuvinteSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    nome = serializers.SerializerMethodField()

    def get_user(self, instance):
        return instance.user.email

    def get_nome(self, instance):
        return f"{instance.primeiro_nome} {instance.sobrenome}"

    class Meta:
        model = Listener
        fields = ["id", "user", "phone", "nome"]


class ArtistaSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    def get_user(self, instance):
        return instance.user.email

    class Meta:
        model = Artist
        fields = "__all__"


class SegueSerializer(serializers.ModelSerializer):
    artista = serializers.SerializerMethodField()
    ouvinte = serializers.SerializerMethodField()

    def get_artista(self, instance):
        return instance.artista.user.email

    def get_ouvinte(self, instance):
        return instance.ouvinte.user.email
        
    class Meta:
        model = Segue
        fields = "__all__"