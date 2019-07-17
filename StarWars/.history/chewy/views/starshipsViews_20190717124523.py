from django.views.generic.list import ListView
from django.views.generic.base import View
from chewy.models.transport import Starship


class StarshipsListView(View):
    model = Starship
    template_name = "starships/starships.html"
    context_object_name = "starships"

    def get_queryset(self):
        return Starship.objects.all()


class StarshipsView(View):
    model = Starship
    template_name = "starships/starshipsDetails.html"
    context_object_name = "starship"

    def get_queryset(self):
        result = super().get_queryset()
        id = self.kwargs.get("id")
        if id:
            result = Starship.objects.get(id=id)
        else:
            result = None
        return result
