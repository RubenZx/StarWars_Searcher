from django.urls import path
from chewy.views.index import IndexTemplateView
from chewy.views.filmsViews import SearchTemplateView, FilmView


urlpatterns = [
    path("", IndexTemplateView.as_view(), name="index"),
    path("search/", SearchTemplateView.as_view(), name="search_list"),
    path("film/<int:id>/", FilmView.as_view(), name="film"),
    path("films", FilmListView.as_view(), name="film"),
]
