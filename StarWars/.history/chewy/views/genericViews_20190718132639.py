from django.views.generic.base import View
from django.shortcuts import render


def general_get(self, request, model, ctxt, template):
    return render(request, template, context={ctxt: model.objects.all()})


# def getView(self, request, id):
#     return render(
#         request,
#         templaete
#         context={"ctxt": model.objects.get(id=id)},
#     )
