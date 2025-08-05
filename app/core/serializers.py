from accounts.models import CustomUser
from rest_framework import serializers

from core.models import Genre, Movie, Network


class AbstractBaseSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        abstract = True


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("id", "username")


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ("id", "name")


class MovieSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(many=True)

    class Meta:
        model = Movie
        fields = ("id", "title", "year", "genre", "language", "overview", "rating", "running_time")
        read_only_fields = ("id",)

    def create(self, validated_data):
        """
        Create and return a new `Movie` instance, given the validated data.
        Only assign existing genres to the movie, don't create new ones.
        """
        genre_data = validated_data.pop("genre", [])
        movie = Movie.objects.create(**validated_data)

        for genre_name in genre_data:
            genre_obj = Genre.objects.get(name=genre_name["name"])
            movie.genre.add(genre_obj)

        movie.save()
        return movie


class NetworkSerializer(AbstractBaseSerializer):
    class Meta(AbstractBaseSerializer.Meta):
        model = Network
