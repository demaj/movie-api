from rest_framework.routers import SimpleRouter
from datadump.views import GenreViewSet, MovieViewSet

app_name = 'datadump'

router = SimpleRouter()
router.register('genres', GenreViewSet, basename='genres')
router.register('movies', MovieViewSet, basename='movies')

urlpatterns = router.urls
