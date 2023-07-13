from django.test import TestCase
from . import models


class UserTest(TestCase):

    def setUp(self):
        self.email = "example@email.com"
        self.password = "password123"
        self.username = "example"
        self.user = models.User.objects.create(
            email=self.email, password=self.password, username=self.username)

    def test_user_creation(self):
        self.assertEqual(self.email, self.user.email)

    def test_profile_created(self):
        profile = self.user.profile
        self.assertTrue(profile)
