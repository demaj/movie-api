from core.views import GenreViewSet, MovieViewSet, NetworkViewSet, PeriodViewSet
from rest_framework.routers import DefaultRouter, SimpleRouter

app_name = "core"

router = DefaultRouter(trailing_slash=False)
router.register("genres", GenreViewSet, basename="genres")
router.register("movies", MovieViewSet, basename="movies")
router.register("periods", PeriodViewSet, basename="periods")
router.register("networks", NetworkViewSet, basename="networks")

urlpatterns = router.urls
