from django.views.generic.base import View
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin

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


class adminView(LoginRequiredMixin, View):
    login_url = "/login"
    redirect_field_name = "redirect_to"

    def get(self, request):
        return render(request, "admin.html", context={"models": MODELS})
