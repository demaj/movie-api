from factory.django import DjangoModelFactory

from datadump.models import Genre, Movie


class GenreFactory(DjangoModelFactory):

    class Meta:
        model = Genre

    name = 'Comic'


class MovieFactory(DjangoModelFactory):

    class Meta:
        model = Movie

    title = "The Unbearable Lightness of Being"
    year = 1995
    genre = GenreFactory()

