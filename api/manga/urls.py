from django.urls import path
from . import views


urlpatterns = [
    path("", views.ListMangaApiView.as_view(), name="")
]
