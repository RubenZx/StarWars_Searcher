from django.views.generic.base import TemplateView
from chewy.models.historic import Historic
from django.db.models import Count


class IndexTemplateView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        historic = Historic.objects.filter()
        historic.

        return context
