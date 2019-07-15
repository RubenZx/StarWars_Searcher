from django.views.generic.list import ListView
from chewy.models.film import Film


class FilmListView(ListView):
    model = Film
    template_name = "categories/films.html"
    context_object_name = "film"

    def get_queryset(self):
        return Film.objects.all()
