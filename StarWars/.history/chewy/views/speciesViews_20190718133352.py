from chewy.models.species import Species
from chewy.views.genericViews import generalGet


class SpeciesListView:
    gg = generalGet(Species.objects.all(), "species", "species/species.html")
    gg.get()


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