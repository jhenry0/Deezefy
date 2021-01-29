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
    user = serializers.SerializerMethodField(read_only=True)
    user_email = serializers.EmailField(write_only=True)
    nome = serializers.SerializerMethodField()

    def create(self, validated_data):
        user = User.objects.get(email=validated_data["user_email"])
        instance = Listener.objects.create(
            phone=validated_data["phone"], 
            primeiro_nome=validated_data["primeiro_nome"],
            sobrenome=validated_data["sobrenome"],
            user=user
            ) 
        return instance

    def update(self, instance, validated_data):
        user = User.objects.get(email=validated_data["user_email"])
        Listener.objects.filter(id=instance.id).update(
            phone=validated_data["phone"], 
            primeiro_nome=validated_data["primeiro_nome"],
            sobrenome=validated_data["sobrenome"],
            user=user
        ) 

        return Listener.objects.filter(id=instance.id).first()

    def get_user(self, instance):
        return instance.user.email

    def get_nome(self, instance):
        return f"{instance.primeiro_nome} {instance.sobrenome}"

    class Meta:
        model = Listener
        fields = ["id", "user", "phone", "nome", "user_email", "primeiro_nome", "sobrenome"]


class ArtistaSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField(read_only=True)
    user_email = serializers.EmailField(write_only=True)

    def create(self, validated_data):
        user = User.objects.get(email=validated_data["user_email"])
        instance = Artist.objects.create(
            stage_name=validated_data["stage_name"], 
            biography=validated_data["biography"],
            formation_year=validated_data["formation_year"],
            user=user
            ) 
        return instance

    def update(self, instance, validated_data):
        user = User.objects.get(email=validated_data["user_email"])
        Artist.objects.filter(id=instance.id).update(
            stage_name=validated_data["stage_name"], 
            biography=validated_data["biography"],
            formation_year=validated_data["formation_year"],
            user=user
        )

        return Artist.objects.filter(id=instance.id).first()

    def get_user(self, instance):
        return instance.user.email

    class Meta:
        model = Artist
        fields = ["id", "stage_name", "biography", "formation_year", "user", "user_email"]


class SegueSerializer(serializers.ModelSerializer):
    artista = serializers.SerializerMethodField(read_only=True)
    ouvinte = serializers.SerializerMethodField(read_only=True)
    artista_email = serializers.EmailField(write_only=True)
    ouvinte_email = serializers.EmailField(write_only=True)

    def create(self, validated_data):
        artista = Artist.objects.get(user__email=validated_data["artista_email"])
        ouvinte = Listener.objects.get(user__email=validated_data["ouvinte_email"])
        instance = Segue.objects.create(
            artista=artista,
            ouvinte=ouvinte
            ) 
        return instance

    def update(self, instance, validated_data):
        artista = Artist.objects.get(user__email=validated_data["artista_email"])
        ouvinte = Listener.objects.get(user__email=validated_data["ouvinte_email"])
        Segue.objects.filter(id=instance.id).update(
            artista=artista,
            ouvinte=ouvinte
        )

        return Segue.objects.filter(id=instance.id).first()

    def get_artista(self, instance):
        return instance.artista.user.email

    def get_ouvinte(self, instance):
        return instance.ouvinte.user.email
        
    class Meta:
        model = Segue
        fields = "__all__"