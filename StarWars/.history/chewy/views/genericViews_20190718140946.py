from django.views.generic.base import View
from django.shortcuts import render


class generalGet(View):
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
                kwargs["template"],
                context={kwargs["context_name"]: kwargs["model"].objects.all()},
            )
