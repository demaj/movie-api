from core.filters import GenreFilter, MovieFilter, NetworkFilter
from core.models import Genre, Movie, Network
from core.serializers import GenreSerializer, MovieSerializer, NetworkSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated


class AbstractBaseViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = (DjangoFilterBackend,)

    class Meta:
        abstract = True


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = (DjangoFilterBackend,)
    filterset_class = GenreFilter


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = (DjangoFilterBackend,)
    filterset_class = MovieFilter


class NetworkViewSet(viewsets.ModelViewSet):
    queryset = Network.objects.all()
    serializer_class = NetworkSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = (DjangoFilterBackend,)
    filterset_class = NetworkFilter
