from django.views.generic.base import View
from django.shortcuts import render
from chewy.models.planet import Planet


class PlanetsListView(View):
    def get(self, request):
        return render(
            request, "planets/planets.html", context={"planets": Planet.objects.all()}
        )


class PlanetsView(View):
    def get(self, request, id):
        return render(
            request,
            "planets/planetsDetails.html",
            context={"planet": Planet.objects.get(id=id)},
        )

