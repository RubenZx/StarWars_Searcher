from django.views.generic.list import ListView
from chewy.models.species import Species


class SpeciesListView(ListView):
    model = Species
    template_name = "species/species.html"
    context_object_name = "species"

    def get_queryset(self):
        return Species.objects.all()


class SpeciesView(ListView):
    model = Species
    template_name = "species/speciesDetails.html"
    context_object_name = "species"

    def get_queryset(self):
        id = self.kwargs.get("id")
        if id:
            result = Species.objects.get(id=id)
        else:
            result = None
        return result
