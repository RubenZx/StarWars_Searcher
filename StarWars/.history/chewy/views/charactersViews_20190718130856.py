from django.views.generic.base import View
from django.shortcuts import render

from chewy.models.people import People


class CharactersListView(View):
    def get(self, request):
        return render(
            request,
            "characters/characters.html",
            context={"characters": People.objects.all()},
        )


class CharacterView(View):
    def get(request, id):
        return render(
            request,
            "characters/charactersDetails.html",
            context={"charac": People.objects.get(id=id)},
        )
