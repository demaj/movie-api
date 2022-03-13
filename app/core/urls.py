from core.views import GenreViewSet, MovieViewSet
from rest_framework.routers import DefaultRouter, SimpleRouter

app_name = "core"

router = DefaultRouter(trailing_slash=False)
router.register("genres", GenreViewSet, basename="genres")
router.register("movies", MovieViewSet, basename="movies")

urlpatterns = router.urls
