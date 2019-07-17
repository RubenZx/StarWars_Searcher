from django.views.generic.list import ListView
from chewy.models.planet import Planet


class PlanetsListView(ListView):
    model = Planet
    template_name = "planets/planets.html"
    context_object_name = "planets"

    def get_queryset(self):
        return Planet.objects.all()


class CharacterView(ListView):
    model = Planet
    template_name = "characters/charactersDetails.html"
    context_object_name = "charac"

    def get_queryset(self):
        id = self.kwargs.get("id")
        if id:
            result = Planet.objects.get(id=id)

        else:
            result = None
        return result
