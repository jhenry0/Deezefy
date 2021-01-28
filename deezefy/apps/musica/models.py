from django.db import models

from apps.accounts.models import Listener, Artist
# Create your models here.

class Musica(models.Model):
    nome = models.CharField(max_length=50, verbose_name="Nome da musica")
    duracao = models.IntegerField(verbose_name="Duração da musica")

    class Meta:
        verbose_name="Musica"
        verbose_name_plural="Musicas"

    def __str__(self):
        return self.nome


class Curte(models.Model):
    ouvinte = models.ForeignKey(Listener, on_delete=models.CASCADE, related_name="Curto", verbose_name="Ouvinte")
    musica = models.ForeignKey(Musica, on_delete=models.CASCADE, related_name="Seguidor", verbose_name="Musica")

    class Meta:
        verbose_name="Curte"
        verbose_name_plural="Curtem"

    def __str__(self):
        return f"{self.ouvinte} - {self.musica}"


class Playlist(models.Model):
    nome = models.CharField(max_length=50, verbose_name="Nome da musica")
    enumeração = models.BooleanField(verbose_name="enumeração")

    class Meta:
        verbose_name="Playlist"
        verbose_name_plural="Playlists"

    def __str__(self):
        return self.nome


class Cria(models.Model):
    ouvinte = models.ForeignKey(Listener, on_delete=models.CASCADE, related_name="criador", verbose_name="Ouvinte")
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE, related_name="criada", verbose_name="Playlist")
    data_de_criacao = models.DateField(verbose_name="Data de criação")

    class Meta:
        verbose_name="Cria"
        verbose_name_plural="Criadas"

    def __str__(self):
        return f"{self.ouvinte} - {self.playlist}"


class Grava(models.Model):
    artista = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name="Artista", verbose_name="artista")
    musica = models.ForeignKey(Musica, on_delete=models.CASCADE, related_name="Musica", verbose_name="Musica")

    class Meta:
        verbose_name="Curte"
        verbose_name_plural="Curtem"

    def __str__(self):
        return f"{self.artista} - {self.musica}"