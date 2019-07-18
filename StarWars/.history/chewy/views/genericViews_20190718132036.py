from django.views.generic.base import View
from django.shortcuts import render


class ModelListView(View):
    def get(self, request):
        return render(
            request, "planets/planets.html", context={"planets": Planet.objects.all()}
        )


class ModelView(View):
    def get(self, request, id):
        return render(
            request,
            "planets/planetsDetails.html",
            context={"planet": Planet.objects.get(id=id)},
        )
