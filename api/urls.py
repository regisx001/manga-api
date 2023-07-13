from django.urls import path, include


urlpatterns = [
    path("manga/", include("api.manga.urls"), name="")
]
