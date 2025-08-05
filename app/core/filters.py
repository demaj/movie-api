from django_filters import rest_framework as filters

from core.models import Genre, Movie, Network


class GenreFilter(filters.FilterSet):
    class Meta:
        model = Genre
        fields = ("name",)


class MovieFilter(filters.FilterSet):
    year = filters.NumberFilter(field_name="year")
    rating = filters.NumberFilter(field_name="rating")

    class Meta:
        model = Movie
        fields = {
            "title": ("iexact", "icontains"),
            "year": ("lt", "gt", "lte", "gte"),
            "rating": ("lt", "gt", "lte", "gte"),
        }


class NetworkFilter(filters.FilterSet):
    name_in = filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = Network
        fields = ("name", "country")
