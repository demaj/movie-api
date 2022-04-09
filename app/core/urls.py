from core.views import GenreViewSet, MovieViewSet, NetworkViewSet
from rest_framework.routers import DefaultRouter

app_name = "core"

router = DefaultRouter(trailing_slash=False)
router.register("genres", GenreViewSet, basename="genres")
router.register("movies", MovieViewSet, basename="movies")
router.register("networks", NetworkViewSet, basename="networks")

urlpatterns = router.urls
