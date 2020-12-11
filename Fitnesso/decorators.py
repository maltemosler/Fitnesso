from django.core.handlers.wsgi import WSGIRequest
from django.http import Http404


def only_ajax(func):
    def wrapper(request: WSGIRequest, *args, **kwargs):
        if request.is_ajax() and request.method == "POST":
            return func(request, *args, **kwargs)
        else:
            raise Http404

    return wrapper
