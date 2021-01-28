from django.contrib import admin

from .models import Musica, Curte, Cria, Playlist, Grava

# Register your models here.
admin.site.register(Musica)
admin.site.register(Curte)
admin.site.register(Cria)
admin.site.register(Playlist)
admin.site.register(Grava)