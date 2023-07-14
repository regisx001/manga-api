from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify


from django.contrib.admin.decorators import display
from django.template.loader import get_template


class Manga(models.Model):

    MANGA_STATUS = (
        ("unknown", "unknown"),
        ("ongoing", "ongoing"),
        ("completed", "completed")
    )

    slug = models.CharField(unique=True, max_length=200)
    name = models.CharField(max_length=300, unique=True)
    poster = models.ImageField(
        upload_to="posters/%Y/%m/%d", max_length=400, null=True)
    description = models.TextField(blank=True, default="")
    rating = models.DecimalField(default=0,
                                 blank=True, decimal_places=2, max_digits=10)
    author = models.CharField(max_length=200, blank=True)
    type = models.CharField(max_length=200, blank=True)
    release_year = models.CharField(blank=True, max_length=100)
    status = models.CharField(choices=MANGA_STATUS, max_length=100, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    @display(description='Poster Preview')
    def poster_preview(self):
        return get_template('img_preview.html').render({
            'field_name': 'poster',
            'src': self.poster.url if self.poster else None,
        })


@receiver(pre_save, sender=Manga)
def slugify_manga_name(sender, instance: Manga, **kwargs):
    instance.slug = slugify(instance.name)
