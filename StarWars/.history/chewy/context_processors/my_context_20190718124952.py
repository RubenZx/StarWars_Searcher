from django.contrib.sessions.models import Session


def my_context(request):
    context_data = dict()
    s = Session.objects.get(pk=request.session_key)
    context_data["last_visits"] = ["last_pages"][-10:]
    return context_data
