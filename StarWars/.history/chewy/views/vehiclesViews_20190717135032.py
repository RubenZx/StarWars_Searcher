from django.views.generic.base import View
from django.shortcuts import render

from chewy.models.transport import Vehicle


class VehiclesListView(View):
    def get(self, request):
        return render(
            request,
            "starships/veichles.html",
            context={"vehicles": Vehicle.objects.all()},
        )


class VehiclesView(View):
    def get(self, request, id):
        return render(
            request,
            "vehicles/vehiclesDetails.html",
            context={"vehicle": Vehicle.objects.get(id=id)},
        )
