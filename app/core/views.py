from core.filters import GenreFilter, MovieFilter, NetworkFilter, PeriodFilter
from core.models import Genre, Movie, Network, Period
from core.serializers import (
    GenreSerializer,
    MovieSerializer,
    NetworkSerializer,
    PeriodSerializer,
)
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets


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


class PeriodViewSet(viewsets.ModelViewSet):
    queryset = Period.objects.all()
    serializer_class = PeriodSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = PeriodFilter


class NetworkViewSet(viewsets.ModelViewSet):
    queryset = Network.objects.all()
    serializer_class = NetworkSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = NetworkFilter
