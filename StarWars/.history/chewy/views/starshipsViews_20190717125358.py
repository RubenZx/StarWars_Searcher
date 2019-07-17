from django.views.generic.list import ListView
from django.views.generic.base import View
from django.shortcuts import render
from django.template import loader

from chewy.models.transport import Starship


class StarshipsListView(View):
    def get(self, request):
        return render(
            request,
            "starships/starships.html",
            context={"starships": Starship.objects.all()},
        )


class StarshipsView(View):
    def get(self, request):
        id = self.kwargs.get("id")

        return render(
            request,
            "starships/starshipsDetails.html",
            context={"starchip": Starship.objects.get(id=id)},
        )
