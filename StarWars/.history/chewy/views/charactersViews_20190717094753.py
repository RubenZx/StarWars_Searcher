from django.views.generic.list import ListView
from django.core import serializers
from chewy.models.people import People


class CharactersListView(ListView):
    model = People
    template_name = "characters/characters.html"
    context_object_name = "characters"

    def get_queryset(self):
        return People.objects.all()


class CharacterView(ListView):
    model = People
    template_name = "characters/charactersDetails.html"
    context_object_name = "charac"

    def get_queryset(self):
        id = self.kwargs.get("id")

        if id:
            result = People._meta.get(id=id).get_fields()
            # result = People.objects.get(id=id)
        else:
            result = None
        return result
