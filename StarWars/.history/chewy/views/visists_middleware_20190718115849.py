def simple_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = get_response(request)

        request_path = request.get_full_path()
        request.session["last_pages"].append(request_path)
        return request.session["last_pages"][-10:]

        # Code to be executed for each request/response after
        # the view is called.

        return response

    return middleware
