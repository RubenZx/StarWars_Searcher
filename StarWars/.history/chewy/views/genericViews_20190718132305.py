from django.views.generic.base import View
from django.shortcuts import render


def getList(self, request, model, ctxt, template):
    return render(request, template, context={ctxt: model.objects.all()})


class ModelView(View):
    def get(self, request, id):
        return render(
            request,
            "planets/planetsDetails.html",
            context={"ctxt": model.objects.get(id=id)},
        )
