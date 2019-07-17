from django.views.generic.list import ListView
from chewy.models.transport import Starship


class StarshipsListView(ListView):
    model = Starship
    template_name = "starships/starships.html"
    context_object_name = "starships"

    def get_queryset(self):
        return Starship.objects.all()


class StarshipsView(ListView):
    model = Starship
    template_name = "starships/speciesDetails.html"
    context_object_name = "starship"

    def get_queryset(self):
        id = self.kwargs.get("id")
        if id:
            result = Starship.objects.get(id=id)
        else:
            result = None
        return result
