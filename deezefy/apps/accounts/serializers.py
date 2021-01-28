from datetime import datetime
from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from .models import User, Listener, Artist


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
    
    class Meta:
        model = Listener
        fields = "__all__"

class ArtistaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Artist
        fields = "__all__"