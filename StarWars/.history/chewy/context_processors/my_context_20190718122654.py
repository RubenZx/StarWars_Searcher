def my_context(request):
    context_data = dict()
    context_data["last_visits"] = request.session["last_pages"][-10:]
    return context_data
