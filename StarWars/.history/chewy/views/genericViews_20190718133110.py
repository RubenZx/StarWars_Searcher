from django.views.generic.base import View
from django.shortcuts import render


class generalGet(View):
    def __init__(self, model, context_name, template):
        self.model = model
        self.context_name = context_name
        self.template = template

    def get(self, request, model, ctxt, template):
        return render(request, template, context={ctxt: model.objects.all()})


# def getView(self, request, id):
#     return render(
#         request,
#         templaete
#         context={"ctxt": model.objects.get(id=id)},
#     )
