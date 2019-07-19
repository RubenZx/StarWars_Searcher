from django.views.generic.base import View
from django.shortcuts import render


class adminView(View):
    def get(self, request):
        if request.user.is_authenticated():
            return render()
