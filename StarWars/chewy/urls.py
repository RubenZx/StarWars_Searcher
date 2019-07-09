from django.urls import path
from .views.index import index

# from .views.filmsViews import filmsViews

# views.app_name = "chewy"

urlpatterns = [
    path("", index, name="index"),
    #  path("films/", filmsViews, name="search")
]
