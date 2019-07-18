from django.views.generic.base import View
from django.shortcuts import render

from django.views.generic.list import ListView
from chewy.models.people import People


class CharactersListView(View):
    def get(self, request):
        return render(
            request,
            "characters/characters.html",
            context={"characters": People.objects.all()},
        )


class CharacterView(ListView):
    model = People
    template_name = "characters/charactersDetails.html"
    context_object_name = "charac"

    def get_queryset(self):
        id = self.kwargs.get("id")
        if id:
            result = People.objects.get(id=id)

        else:
            result = None
        return result
