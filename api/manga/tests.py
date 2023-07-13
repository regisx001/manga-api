from django.test import TestCase
from rest_framework.test import APIRequestFactory
from api.manga import models

factory = APIRequestFactory()


class MangaTest(TestCase):
    def setUp(self):
        models.Manga.objects.create(slug="one-piece", name="One Piece")

    def test_is_created(self):
        one_piece = models.Manga.objects.get(slug="one-piece")
        self.assertEqual(one_piece.name, "One Piece")
