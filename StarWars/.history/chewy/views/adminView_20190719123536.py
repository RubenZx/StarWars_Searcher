from django.views.generic.base import View
from django.shortcuts import render

from chewy.models.film import Film
from chewy.models.people import People
from chewy.models.planet import Planet
from chewy.models.species import Species
from chewy.models.transport import Starship, Vehicle


MODELS = {
    "Planets": Planet.objects.count(),
    "People": People.objects.count(),
    "Starships": Starship.objects.count(),
    "Vehicles": Vehicle.objects.count(),
    "Species": Species.objects.count(),
    "Films": Film.objects.count(),
}


class adminView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, "admin.html", context={"models": MODELS})
