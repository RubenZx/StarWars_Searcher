from django.views.generic.base import TemplateView
from chewy.models.models import Film


class IndexTemplateView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Films"] = Film.objects.all()

        return context

    def get_name(film) -> str:
        film.get_name()


# def index(request):
# return render(request, "index.html")
