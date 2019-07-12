from django.views.generic.base import TemplateView
from django.db.models import Q
from chewy.models.models import Film


class SearchTemplateView(TemplateView):
    template_name = "films/search_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get("search", None)

        films = Film.objects.all()
        if query is not None:
            context["films"] = films.filter(
                title__icontains=query,
                opening_crawl__icontains=query),
                director__icontains=query),
                producer__icontains=query),
                release_date__icontains=query),
            )  # Filter to find the films that containts the request

        return context
