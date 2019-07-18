from django.views.generic.base import View
from django.shortcuts import render
from chewy.models.planet import Planet


class PlanetsListView(View):
    def get(self, request):
        return render(
            request, "planets/planets.html", context={"planets": Planet.objects.all()}
        )


class PlanetsView(ListView):
    model = Planet
    template_name = "planets/planetsDetails.html"
    context_object_name = "planet"

    def get_queryset(self):
        id = self.kwargs.get("id")
        if id:
            result = Planet.objects.get(id=id)

        else:
            result = None
        return result
