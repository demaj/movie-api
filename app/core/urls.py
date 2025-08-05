from rest_framework.routers import DefaultRouter

from core.views import GenreViewSet, MovieViewSet, NetworkViewSet

app_name = "core"

router = DefaultRouter(trailing_slash=False)
router.register(r"genres", GenreViewSet, basename="genres")
router.register(r"movies", MovieViewSet, basename="movies")
router.register(r"networks", NetworkViewSet, basename="networks")

urlpatterns = router.urls
