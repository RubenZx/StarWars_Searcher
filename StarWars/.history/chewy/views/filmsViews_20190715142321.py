from django.views.generic.list import ListView
from django.db.models import Q
from chewy.models.film import Film
from chewy.models.historic import Historic


class SearchTemplateView(ListView):
    model = Film
    template_name = "films/search_list.html"
    context_object_name = "films"

    def get_queryset(self):
        result = super().get_queryset()
        query = self.request.GET.get("q")
        if query:
            result = Film.objects.filter(
                Q(title__icontains=query)
                | Q(opening_crawl__icontains=query)
                | Q(director__icontains=query)
                | Q(producer__icontains=query)
                | Q(release_date__icontains=query)
                | Q(characters__name__icontains=query)
                | Q(planets__name__icontains=query)
            ).distinct()
            for film in result:
                Historic.objects.create(film=film)
        else:
            result = None
        return result


class FilmView(ListView):
    model = Film
    template_name = "films/film.html"
    context_object_name = "film"

    def get_queryset(self):
        result = super().get_queryset()
        id = self.kwargs.get("id")
        if id:
            result = Film.objects.get(id=id)
        else:
            result = None
        return result

    def get_context_data(self, **kwargs):
        context = super(FilmView, self).get_context_data(**kwargs)
        ctxt = Film.objects.get(id=id)
        context["characters"] = ctxt.characters.all()

        return context


class FilmListView(ListView):
    model = Film
    template_name = "categories/films.html"
    context_object_name = "film"

    def get_queryset(self):
        return Film.objects.all()
