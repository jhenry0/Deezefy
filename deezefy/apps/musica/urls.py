from rest_framework import routers

from . import api

app_name = "musica"

router = routers.SimpleRouter()
router.register("musica", api.MusicaViewSet, basename="musica")
router.register("curte", api.CurteViewSet, basename="curte")
router.register("playlist", api.PlaylistViewSet, basename="playlist")
router.register("cria", api.CriaViewSet, basename="cria")
router.register("grava", api.GravaViewSet, basename="grava")

urlpatterns = router.urls