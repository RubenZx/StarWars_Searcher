from django.views.generic.base import View
from django.shortcuts import render

from chewy.models.film import Film
from chewy.models.people import People
from chewy.models.planet import Planet
from chewy.models.species import Species
from chewy.models.transport import Starship, Vehicle


MODELS = {
    "Planet": Planet.objects.count(),
    "People": People.objects.count(),
    "Starship": Starship.objects.count(),
    "Vehicle": Vehicle.objects.count(),
    "Species": Species.objects.count(),
    "Film": Film.objects.count(),
}


class adminView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, "admin.html", context={"models": MODELS})
