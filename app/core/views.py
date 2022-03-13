from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from core.filters import GenreFilter, MovieFilter
from core.models import Genre, Movie
from core.serializers import GenreSerializer, MovieSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = GenreFilter


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = MovieFilter
