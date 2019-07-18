from django.urls import path
from chewy.views.index import IndexTemplateView
from chewy.views.filmsViews import SearchTemplateView, FilmView, FilmListView
from chewy.views.genericViews import generalGet
from chewy.models.film import Film
from chewy.models.people import People
from chewy.models.planet import Planet
from chewy.models.species import Species
from chewy.models.transport import Starship, Vehicle


urlpatterns = [
    path("", IndexTemplateView.as_view(), name="index"),
    path("search/", SearchTemplateView.as_view(), name="search_list"),
    path("film/<int:id>/", FilmView.as_view(), name="film"),
    path(
        "films",
        generalGet.as_view(),
        {
            "name": "films",
            "model": Film,
            "context_name": "film",
            "template": "films/films.html",
        },
        FilmListView.as_view(),
        name="film",
    ),
    path(
        "characters",
        generalGet.as_view(),
        {
            "name": "characters",
            "model": People,
            "context_name": "characters",
            "template": "characters/characters.html",
        },
    ),
    path(
        "characters/<int:id>/",
        generalGet.as_view(),
        {
            "name": "characters",
            "model": People,
            "context_name": "charac",
            "template": "characters/charactersDetails.html",
        },
    ),
    path(
        "planets",
        generalGet.as_view(),
        {
            "name": "planets",
            "model": Planet,
            "context_name": "planet",
            "template": "planets/planets.html",
        },
    ),
    path(
        "planets/<int:id>/",
        generalGet.as_view(),
        {
            "name": "planets",
            "model": Planet,
            "context_name": "planet",
            "template": "planets/planetsDetails.html",
        },
    ),
    path(
        "species",
        generalGet.as_view(),
        {
            "name": "species",
            "model": Species,
            "context_name": "species",
            "template": "species/species.html",
        },
    ),
    path(
        "species/<int:id>/",
        generalGet.as_view(),
        {
            "name": "species",
            "model": Species,
            "context_name": "species",
            "template": "species/speciesDetails.html",
        },
    ),
    path(
        "starships",
        generalGet.as_view(),
        {
            "name": "starships",
            "model": Starship,
            "context_name": "starships",
            "template": "starships/starships.html",
        },
    ),
    path(
        "starships/<int:id>/",
        generalGet.as_view(),
        {
            "name": "starships",
            "model": Starship,
            "context_name": "starship",
            "template": "starships/starshipsDetails.html",
        },
    ),
    path(
        "vehicles",
        generalGet.as_view(),
        {
            "name": "vehicles",
            "model": Vehicle,
            "context_name": "vehicles",
            "template": "vehicles/vehicles.html",
        },
    ),
    path(
        "vehicles/<int:id>/",
        generalGet.as_view(),
        {
            "name": "vehicle",
            "model": Vehicle,
            "context_name": "vehicle",
            "template": "vehicles/vehiclesDetails.html",
        },
    ),
]
