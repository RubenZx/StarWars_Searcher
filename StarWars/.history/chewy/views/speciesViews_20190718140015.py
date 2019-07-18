from chewy.models.species import Species
from chewy.views.genericViews import generalGet


class SpeciesListView(generalGet):
    def __init__(self):
        super(SpeciesListView, self).__init__(
            Species, "species", "species/species.html"
        )


class SpeciesView(generalGet):
    def __init__(self):
        super(SpeciesView, self).__init__(
            Species, "species", "species/speciesDetails.html"
        )
