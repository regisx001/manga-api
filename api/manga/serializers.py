from rest_framework import serializers
from . import models


class MangaSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Manga
        fields = "__all__"
