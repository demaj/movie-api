from django_filters import rest_framework as filters
from core.models import Genre, Movie


class GenreFilter(filters.FilterSet):

    class Meta:
        model = Genre
        fields = ('name',)


class MovieFilter(filters.FilterSet):
    rating = filters.NumberFilter(field_name="rating")

    class Meta:
        model = Movie
        fields = {
            'title': ('exact', 'contains'),
            'rating': ('lt', 'gt', 'lte', 'gte')
        }
