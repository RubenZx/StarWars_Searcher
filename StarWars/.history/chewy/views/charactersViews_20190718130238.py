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
    def get(self, request):
        return render(
            request,
            "characters/charactersDetails.html",
            context={"charac": self.get_queryset()},
        )

    def get_queryset(self):
        id = self.kwargs.get("id")
        if id:
            result = People.objects.get(id=id)

        else:
            result = None
        return result
