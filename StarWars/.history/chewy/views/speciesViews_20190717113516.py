from django.views.generic.list import ListView
from chewy.models.species import Species


class PlanetsListView(ListView):
    model = Species
    template_name = "species/Species.html"
    context_object_name = "species"

    def get_queryset(self):
        return Species.objects.all()


class PlanetsView(ListView):
    model = Planet
    template_name = "planets/planetsDetails.html"
    context_object_name = "planet"

    def get_queryset(self):
        id = self.kwargs.get("id")
        if id:
            result = Planet.objects.get(id=id)

        else:
            result = None
        return result
