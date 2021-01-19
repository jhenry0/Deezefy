from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    birthday = models.DateField(blank=True, null=True, verbose_name="Dia do nascimento")
    age = models.IntegerField(blank=True, null=True, verbose_name="Idade")

    class Meta:
        verbose_name="Usuario"
        verbose_name_plural="Usuarios"

    def __str__(self):
        return self.password


class Artist(models.Model):
    stage_name = models.CharField(max_length=200, verbose_name="Nome artistico")
    biography = models.TextField(verbose_name="Biografia")
    formation_year = models.IntegerField(verbose_name="Ano de formação")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario")

    class Meta:
        verbose_name="Artista"
        verbose_name_plural="Artistas"

    def __str__(self):
        return self.stage_name


class Listener(models.Model):
    phone = models.CharField(max_length=15, blank=True, verbose_name="Numero de Telefone")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usario")

    class Meta:
        verbose_name="Ouvinte"
        verbose_name_plural="Ouvintes"

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


