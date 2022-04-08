from accounts.models import CustomUser
from core.models import Genre, Movie, Network, Period
from rest_framework import serializers


class BaseSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        abstract = True


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("id", "username")


class GenreSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = Genre


class MovieSerializer(serializers.ModelSerializer):
    genre = serializers.StringRelatedField()

    class Meta:
        model = Movie
        fields = ("title", "year", "genre", "language", "overview", "rating")


class PeriodSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = Period


class NetworkSerializer(serializers.ModelSerializer):
    start_period = serializers.StringRelatedField()
    end_period = serializers.StringRelatedField()

    class Meta:
        model = Network
        fields = ("name", "country", "start_period", "end_period")
