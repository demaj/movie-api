from django.urls import reverse
from faker import Faker
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from datadump.tests.factories import GenreFactory


class GenreViewSetTestCase(APITestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.genre_object = GenreFactory.build()
        cls.genre_saved = GenreFactory.create()
        cls.client = APIClient()
        cls.faker_obj = Faker()

    def test_genres_list(self):
        """ Ensure we can get the list of all genre objects. """
        genre_list = [{"name": self.genre_object.name}]
        response = self.client.get(
            path=reverse('datadump:genres-list'),
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_genres_create(self):
        """ Ensure we can create a new genre object. """
        payload = {"name": self.genre_object.name}
        response = self.client.post(
            path=reverse('datadump:genres-list'),
            data=payload,
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_genres_read(self):
        pass

    def test_genres_update(self):
        pass

    def test_genres_delete(self):
        pass


# class MovieViewSetTestCase(APITestCase):
#
#     @classmethod
#     def setUpClass(cls):
#         super().setUpClass()
#         cls.genre_object = MovieFactory.build()
#         cls.genre_saved = MovieFactory.create()
#         cls.client = APIClient()
#         cls.faker_obj = Faker()
#
#     def test_movies_list(self):
#         pass
