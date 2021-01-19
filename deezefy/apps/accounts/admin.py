from django.contrib import admin
from .models import User, Artist, Listener

# Register your models here.
class ArtistInline(admin.StackedInline):
    model = Artist
    fk_name = "user"
    extra= 0

class Listener(admin.StackedInline):
    model = Listener


    
admin.site.register(User)
admin.site.register(Artist)
admin.site.register(Listener)