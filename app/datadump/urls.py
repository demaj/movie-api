from rest_framework.routers import SimpleRouter, DefaultRouter
from datadump.views import GenreViewSet, MovieViewSet

app_name = 'datadump'

router = DefaultRouter(trailing_slash=False)
router.register('genres', GenreViewSet, basename='genres')
router.register('movies', MovieViewSet, basename='movies')

urlpatterns = router.urls
