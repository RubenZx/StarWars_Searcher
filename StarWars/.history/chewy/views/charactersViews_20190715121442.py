from django.views.generic.list import ListView
from chewy.models.people import People


class CharacaterListView(ListView):
    model = People
    template_name = "categories/characters.html"
    context_object_name = "characters"

    def get_queryset(self):
        return People.objects.all()