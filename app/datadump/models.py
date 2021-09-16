import uuid

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Genre(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        db_index=True,
    )
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Genre"
        verbose_name_plural = "Genres"
        ordering = ['name']
        indexes = [
            models.Index(fields=['id', 'name'], name='genre_id_name_idx'),
        ]

    def __str__(self):
        return self.name


class Movie(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        db_index=True,
    )
    title = models.CharField(max_length=255)
    year = models.PositiveIntegerField()
    genre = models.ForeignKey(
        Genre,
        on_delete=models.CASCADE,
        related_name='movies'
    )
    language = models.CharField(max_length=2)
    overview = models.TextField()
    rating = models.PositiveIntegerField(
        default=1,
        validators=[MinValueValidator(1), MaxValueValidator(100)],
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = "Movie"
        verbose_name_plural = "Movies"
        ordering = ['-year', 'title']
        indexes = [
            models.Index(fields=['id', 'title'], name='movie_id_title_idx'),
            models.Index(fields=['id', 'genre'], name='movie_id_genre_idx'),
        ]

    def __str__(self):
        return self.title
