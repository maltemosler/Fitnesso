from django.core.handlers.wsgi import WSGIRequest
from django.http import Http404, HttpResponseServerError


def only_ajax(func):
    def wrapper(request: WSGIRequest, *args, **kwargs):
        if request.is_ajax() and request.method == "POST":
            return func(request, *args, **kwargs)
        else:
            raise Http404

    return wrapper


def validate_goal_user_rights(view):
    def _view(request: WSGIRequest, *args, **kwargs):
        if request.user.fitnessouser.is_trainer or int(request.POST.get("user_id", "")) == int(request.user.id):
            print("permitted user to change goal.")
            return view(request, *args, **kwargs)
        else:
            print("validation failed")
            return HttpResponseServerError()
    return _view
