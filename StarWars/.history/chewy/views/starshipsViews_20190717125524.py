from django.views.generic.list import ListView
from django.views.generic.base import View
from django.shortcuts import render
from django.template import loader

from chewy.models.transport import Starship


class StarshipsListView(View):
    def get(request):
        return render(
            request,
            "starships/starships.html",
            context={"starships": Starship.objects.all()},
        )


class StarshipsView(View):
    def get(request, id):
        return render(
            request,
            "starships/starshipsDetails.html",
            context={"starship": Starship.objects.get(id=id)},
        )
