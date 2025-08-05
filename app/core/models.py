import uuid

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from config.settings import base as settings
from core.fields import CountryField
from core.utils.utils import current_year, year_choices


class AbstractBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.RESTRICT,
        related_name="%(app_label)s_%(class)s_created_by",
        null=True,
    )
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.RESTRICT,
        related_name="%(app_label)s_%(class)s_updated_by",
        null=True,
    )
    deleted_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.RESTRICT,
        related_name="%(app_label)s_%(class)s_deleted_by",
        null=True,
    )

    class Meta:
        abstract = True
        get_latest_by = "updated_at"
        ordering = ("-updated_at", "-created_at")


class Genre(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    name = models.CharField(max_length=200, unique=True)

    class Meta:
        ordering = ["name"]
        indexes = [
            models.Index(fields=["id", "name"], name="genre_id_name_idx"),
        ]

    def __str__(self):
        return self.name


class Company(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    name = models.CharField(max_length=64)
    country = CountryField()
    headquarters = models.CharField(max_length=128)
    homepage = models.URLField()

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"
        ordering = ["name"]
        indexes = [
            models.Index(fields=["id", "name"], name="company_id_name_idx"),
        ]

    def __str__(self):
        return f"{self.name} : {self.homepage}"


class Movie(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    title = models.CharField(max_length=255)
    year = models.PositiveSmallIntegerField("year", choices=year_choices(), default=current_year())
    genre = models.ManyToManyField(Genre, related_name="movies", related_query_name="movie")
    language = CountryField()
    overview = models.TextField()
    rating = models.PositiveSmallIntegerField(
        default=50,
        validators=[MinValueValidator(1), MaxValueValidator(100)],
        null=True,
        blank=True,
    )
    running_time = models.PositiveSmallIntegerField("time")

    class Meta:
        unique_together = ("title", "year")
        ordering = ("-year", "title")
        indexes = [
            models.Index(fields=["id", "title"], name="movie_id_title_idx"),
        ]

    def __str__(self):
        return f"{self.title} ({self.year})"


class Network(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    name = models.CharField(max_length=64)
    country = CountryField()
    headquarters = models.CharField(max_length=128)
    homepage = models.URLField()

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} : {self.homepage}"
