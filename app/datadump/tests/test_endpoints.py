from django.urls import reverse
from faker import Faker
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from datadump.tests.factories import GenreFactory


class GenreViewSetTestCase(APITestCase):
    base_url = reverse('genres')

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.genre_object = GenreFactory.build()
        cls.genre_saved = GenreFactory.create()
        cls.client = APIClient()
        cls.faker_obj = Faker()

    def test_get_genres_list(self):
        # Prepare data
        genre_list = [{"name": self.genre_object.name}]
        response = self.client.get(
            path=self.base_url,

        )
        breakpoint()
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_genre(self):
        """ Ensure we can create a new genre object. """
        pass
