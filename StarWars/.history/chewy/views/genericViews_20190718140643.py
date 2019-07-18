from django.views.generic.base import View
from django.shortcuts import render


class generalGet(View):
    # def __init__(self, model, context_name, template):
    #     self.model = model
    #     self.context_name = context_name
    #     self.template = template

    def get(self, request, *args, **kwargs):
        if len(kwargs) == 5:
            id_ = kwargs["id"]
            return render(
                request,
                kwargs["template"],
                context={kwargs["context_name"]: kwargs["model"].objects.get(id=id_)},
            )
        else:
            return render(
                request,
                self.template,
                context={self.context_name: self.model.objects.all()},
            )
