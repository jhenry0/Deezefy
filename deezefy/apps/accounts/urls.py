from rest_framework import routers

from . import api

app_name = "accounts"

router = routers.SimpleRouter()
router.register("users", api.UserViewSet, basename="users")
router.register("ouvinte", api.OuvinteViewSet, basename="ouvinte")
router.register("artista", api.ArtistaViewSet, basename="artista")

urlpatterns = router.urls