from django.urls import path
from chewy.views.index import IndexTemplateView
from chewy.views.filmsViews import SearchTemplateView, FilmView, FilmListView
from chewy.views.charactersViews import CharactersListView


urlpatterns = [
    path("", IndexTemplateView.as_view(), name="index"),
    path("search/", SearchTemplateView.as_view(), name="search_list"),
    path("film/<int:id>/", FilmView.as_view(), name="film"),
    path("films", FilmListView.as_view(), name="film"),
    path("characters", CharacaterListView.as_view(), name="film"),
]
