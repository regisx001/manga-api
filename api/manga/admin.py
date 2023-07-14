from django.contrib.admin import register
from django.contrib import admin
from unfold.admin import ModelAdmin
from . import models


# Register your models here.


# admin.site.register(models.Manga)

@register(models.Manga)
class MangaAdmin(ModelAdmin):
    list_display = ["name", "slug", "updated_at", "created_at"]
    radio_fields = {"status": admin.VERTICAL}

    fieldsets = (
        ("Basic", {
            "fields": [("name", "status"), "description", "poster",]
        }),
        ("Meta Data", {
            "classes": ["collapse"],
            "fields": [("author", "rating", "type", "release_year"),]
        }

        ),
        # (
        #     "Advanced options",
        #     {
        #         "classes": ["collapse"],
        #         "fields": ["registration_required", "template_name"],
        #     },
        # ),
    )

    exclude = ["slug"]
