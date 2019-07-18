from chewy.models.species import Species
from chewy.views.genericViews import generalGet


class SpeciesListView(generalGet):
    def __init__(self):
        super(SpeciesListView, self).__init__(
            Species, "species", "species/species.html"
        )


class SpeciesView(generalGet):
    def __init__(self):
        super(SpeciesView, self).__init__(Species, "species", "species/species.html")


# class SpeciesView(ListView):
#     model = Species
#     template_name = "species/speciesDetails.html"
#     context_object_name = "species"

#     def get_queryset(self):
#         id = self.kwargs.get("id")
#         if id:
#             result = Species.objects.get(id=id)
#         else:
#             result = None
#         return result
