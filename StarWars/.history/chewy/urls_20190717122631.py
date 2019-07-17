from django.urls import path
from chewy.views.index import IndexTemplateView
from chewy.views.filmsViews import SearchTemplateView, FilmView, FilmListView
from chewy.views.charactersViews import CharactersListView, CharacterView
from chewy.views.planetsViews import PlanetsListView, PlanetsView
from chewy.views.speciesViews import SpeciesListView, SpeciesView
from chewy.views.starshipsViews import StarshipsListView, StarshipsView


urlpatterns = [
    path("", IndexTemplateView.as_view(), name="index"),
    path("search/", SearchTemplateView.as_view(), name="search_list"),
    path("film/<int:id>/", FilmView.as_view(), name="film"),
    path("films", FilmListView.as_view(), name="film"),
    path("characters", CharactersListView.as_view(), name="characters"),
    path("characters/<int:id>/", CharacterView.as_view(), name="characters"),
    path("planets", PlanetsListView.as_view(), name="planets"),
    path("planets/<int:id>/", PlanetsView.as_view(), name="planets"),
    path("species", SpeciesListView.as_view(), name="species"),
    path("species/<int:id>/", SpeciesView.as_view(), name="species"),
    path("starships", StarshipsListView.as_view(), name="starships"),
    path("starships/<int:id>/", StarshipsView.as_view(), name="starship"),
]
