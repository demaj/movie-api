from django.contrib.auth import get_user_model
from django.test import Client, RequestFactory, TestCase


class CustomUserTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()

    def setUpTestData(self):
        user = get_user_model()
        # Create a user
        self.user = user.objects.create_user(
            username="testuser",
            email="user@tests.com",
            password="testpass123",
        )
        # Create a superuser
        self.admin_user = user.objects.create_superuser(
            username="superadmin",
            email="superadmin@tests.com",
            password="testpass123",
        )

    def test_create_user(self):
        self.assertEqual(self.user.username, "testuser")
        self.assertEqual(self.user.email, "user@tests.com")
        self.assertTrue(self.user.is_active)
        self.assertFalse(self.user.is_staff)
        self.assertFalse(self.user.is_superuser)

    def test_create_superuser(self):
        self.assertEqual(self.admin_user.username, "superadmin")
        self.assertEqual(self.admin_user.email, "superadmin@tests.com")
        self.assertTrue(self.admin_user.is_active)
        self.assertTrue(self.admin_user.is_staff)
        self.assertTrue(self.admin_user.is_superuser)
