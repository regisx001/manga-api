from django.db import models
from django.db.models.signals import post_save


class Manga(models.Model):
    slug = models.CharField(unique=True, max_length=200)
    name = models.CharField(max_length=300, unique=True)

    # poster = models.FileField(
    #     upload_to="posters/%Y/%m/%d", max_length=400, null=True)

    # endpoint = models.URLField(unique=True, blank=True, max_length=2000)
    # chapters_endpoint = models.URLField(
    #     unique=True, blank=True, max_length=2000)
    # description = models.TextField(blank=True, default="")
    # rating = models.DecimalField(default=0,
    #                              blank=True, decimal_places=2, max_digits=10)
    # author = models.CharField(max_length=200, blank=True)
    #
    # painter = models.CharField(max_length=200, blank=True)
    # type = models.CharField(max_length=200, blank=True)
    # release_year = models.CharField(blank=True, max_length=100)
    # status = models.CharField(max_length=100, blank=True)
    # updated_at = models.DateTimeField(auto_now=True)
    # uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
