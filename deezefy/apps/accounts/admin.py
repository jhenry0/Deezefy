from django.contrib import admin
from .models import User, Artist, Listener, Segue

# Register your models here.

    
admin.site.register(User)
admin.site.register(Artist)
admin.site.register(Listener)
admin.site.register(Segue)