from django.contrib.admin import register
from unfold.admin import ModelAdmin
from . import models


# Register your models here.


# admin.site.register(models.Manga)

@register(models.Manga)
class MangaAdmin(ModelAdmin):
    pass
