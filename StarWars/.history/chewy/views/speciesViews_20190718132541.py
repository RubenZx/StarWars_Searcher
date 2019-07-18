from django.views.generic.list import ListView
from chewy.models.species import Species
from chewy.views.genericViews import getList


class SpeciesListView:
    def get(self, request):
        return getList(
            request=request,
            model=Species,
            ctxt="species",
            template="species/species.html",
        )


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
