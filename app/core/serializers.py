from accounts.models import CustomUser
from core.models import Genre, Movie, Network
from rest_framework import serializers


class AbstractBaseSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        abstract = True


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("id", "username")


class GenreSerializer(AbstractBaseSerializer):
    class Meta(AbstractBaseSerializer.Meta):
        model = Genre


class MovieSerializer(serializers.ModelSerializer):
    genre = serializers.StringRelatedField()

    class Meta:
        model = Movie
        fields = ("id", "title", "year", "genre", "language", "overview", "rating")


class NetworkSerializer(AbstractBaseSerializer):
    class Meta(AbstractBaseSerializer.Meta):
        model = Network
