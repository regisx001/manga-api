from rest_framework import generics
from . import models, serializers


class ListMangaApiView(generics.ListAPIView):
    queryset = models.Manga.objects.all()
    serializer_class = serializers.MangaSerializer
