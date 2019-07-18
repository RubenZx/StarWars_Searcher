from django.contrib.sessions.backends.db import SessionStore
from django.contrib.sessions.models import Session


class visits_middleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)
        request_path = request.get_full_path()
        key = request.session_key
        try:
            s = Session.objects.get(pk=key)
            s["last_pages"].append(request_path)
            s.save()
        except Exception:
            s = SessionStore()
            s["last_pages"] = [request_path]
            s.save()

        # Code to be executed for each request/response after
        # the view is called.

        return response
