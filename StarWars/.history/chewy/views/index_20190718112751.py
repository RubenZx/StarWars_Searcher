from django.views.generic.base import View
from django.shortcuts import render

from chewy.models.film import Film
from django.db.models import Count


# class IndexTemplateView(ListView):
#     model = Film
#     template_name = "index.html"
#     context_object_name = "films"

#     def get_queryset(self):
#         result = Film.objects.annotate(visits=Count("historic")).order_by("-visits")[:5]
#         return result


class IndexTemplateView(View):
    def get(self, request):
        result = Film.objects.annotate(visits=Count("historic")).order_by("-visits")[:5]
        return render(request, "index.html", context={"films": result})
