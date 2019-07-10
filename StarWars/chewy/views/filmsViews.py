from django.shortcuts import render
from django.db.models import Q
from models.film import Film


class FilmSearch:
    def film_list_search(request):
        query = request.GET.get(
            "search", None
        )  # get(), si search no está en el dict, devuelve None
        films = Film.objects.all()
        if query is not None:
            films = films.filter(
                Q(title__icontains=query)
                | Q(opening_crawl__icontains=query)
                | Q(director__icontains=query)
                | Q(producer__icontains=query)
                | Q(release_date__icontains=query)
            )  # Filtramos para buscar en las peliculas en las que salga la petición

        context = {"films": films}
        return render(request, "films/list_films.html", context)