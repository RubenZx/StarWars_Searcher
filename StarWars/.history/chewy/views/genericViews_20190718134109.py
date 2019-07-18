from django.views.generic.base import View
from django.shortcuts import render


class generalGet(View):
    def __init__(self, objects, context_name, template):
        self.objects = objects
        self.context_name = context_name
        self.template = template

    def get(self, request):
        return render(request, self.template, context={self.context_name: self.objects})

    def get(self, request, id):
        return render(request, self.template, context={self.context_name: self.objects})


# def getView(self, request, id):
#     return render(
#         request,
#         templaete
#         context={"ctxt": model.objects.get(id=id)},
#     )
