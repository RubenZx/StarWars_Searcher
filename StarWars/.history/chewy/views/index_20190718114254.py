from django.views.generic.base import View
from django.shortcuts import render

from chewy.models.film import Film
from django.db.models import Count


class IndexTemplateView(View):
    def get(self, request):
        result = Film.objects.annotate(visits=Count("historic")).order_by("-visits")[:5]
        return render(request, "index.html", context={"films": result})


class Last10PagesVisited(object):
    def proccess_request(self, request):
        request_path = request.get_full_path()
        try:
            request.session["last_visited"] = request.session["currently_visiting"]
        except KeyError:
            # silence the exception - this is the users first request
            pass

        request.session["currently_visiting"] = request_path

