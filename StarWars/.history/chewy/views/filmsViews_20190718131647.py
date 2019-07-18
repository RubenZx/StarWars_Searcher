from django.views.generic.base import View
from django.shortcuts import render
from django.views.generic.list import ListView
from django.db.models import Q
from chewy.models.film import Film
from chewy.models.historic import Historic


class SearchTemplateView(View):
    model = Film
    template_name = "films/search_list.html"
    context_object_name = "films"

    def get(self, request, id):
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
        return render(request, "films/search_list.html", context={"films": result})

    def get_queryset(self):
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


class FilmView(View):
    def get(self, request, id):
        return render(
            request,
            "films/filmsDetails.html",
            context={"film": Film.objects.get(id=id)},
        )


class FilmListView(View):
    def get(self, request):
        return render(request, "films/films.html", context={"film": Film.objects.all()})
