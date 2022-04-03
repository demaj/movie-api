from core.models import Genre, Movie, Network, Period
from django_filters import rest_framework as filters


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


class PeriodFilter(filters.FilterSet):
    year = filters.NumberFilter(field_name="year")
    month = filters.NumberFilter(field_name="month")

    class Meta:
        model = Period
        fields = {
            "year": ("lt", "gt", "lte", "gte"),
            "month": ("lt", "gt", "lte", "gte"),
        }


class NetworkFilter(filters.FilterSet):
    name_in = filters.CharFilter(field_name="name", lookup_expr="icontains")
    start_period__year = filters.NumberFilter(field_name="start_period__year")
    end_period__year = filters.NumberFilter(field_name="end_period__year")

    class Meta:
        model = Network
        fields = ("name", "country")
        fields = {
            "start_period__year": ("lt", "gt", "lte", "gte"),
            "end_period__year": ("lt", "gt", "lte", "gte"),
        }
