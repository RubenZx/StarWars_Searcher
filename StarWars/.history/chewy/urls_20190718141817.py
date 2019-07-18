from django.urls import path
from chewy.views.index import IndexTemplateView
from chewy.views.filmsViews import SearchTemplateView, FilmView, FilmListView
from chewy.views.starshipsViews import StarshipsListView, StarshipsView
from chewy.views.vehiclesViews import VehiclesListView, VehiclesView
from chewy.views.genericViews import generalGet
from chewy.models.people import People
from chewy.models.planet import Planet
from chewy.models.species import Species
from chewy.models.transport import Starship


urlpatterns = [
    path("", IndexTemplateView.as_view(), name="index"),
    path("search/", SearchTemplateView.as_view(), name="search_list"),
    path("film/<int:id>/", FilmView.as_view(), name="film"),
    path("films", FilmListView.as_view(), name="film"),
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
            "model": Starships,
            "context_name": "starships",
            "template": "starships/starships.html",
        },
        StarshipsListView.as_view(),
        name="starships",
    ),
    path("starships/<int:id>/", StarshipsView.as_view(), name="starship"),
    path("vehicles", VehiclesListView.as_view(), name="vehicles"),
    path("vehicles/<int:id>/", VehiclesView.as_view(), name="vehicle"),
]