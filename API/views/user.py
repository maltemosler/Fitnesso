# @only_ajax
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseServerError, JsonResponse

from API.models import FitnessoUser
from API.tasks import validations


def register(request):
    email = request.POST.get("email", "").lower()
    if not validations.validate_email(email):
        return HttpResponseServerError("422-0")
    password = request.POST.get("password", "")
    if not validations.validate_password(password):
        return HttpResponseServerError("422-1")
    vorname = request.POST.get("vorname", "")
    if not validations.validate_first_name(vorname):
        return HttpResponseServerError("422-2")
    nachname = request.POST.get("nachname", "")
    if not validations.validate_last_name(nachname):
        return HttpResponseServerError("422-3")

    user, new = User.objects.get_or_create(username=email)
    if not new:
        print("user not new")
        return HttpResponseServerError("409")
    user.email = email
    user.set_password(password)
    user.save()

    su = FitnessoUser.objects.create(user=user)
    su.vorname = vorname
    su.nachname = nachname
    su.save()

    return HttpResponse("200")


def user_login(request):
    email = request.POST.get("email", "").lower()
    if not validations.validate_email(email):
        return HttpResponseServerError(status=422)

    password = request.POST.get("password", "")
    if not validations.validate_password(password):
        return HttpResponseServerError(status=422)

    try:
        su = User.objects.get(username=email).fitnessouser
    except User.DoesNotExist:
        return HttpResponse(status=403)

    try:
        user = authenticate(request, username=email, password=password)
    except:
        return HttpResponseServerError(status=403)

    if user is not None:
        login(request, user)
        return JsonResponse({"is_trainer": user.fitnessouser.is_trainer, "user_id": user.fitnessouser.user.id})
    else:
        return HttpResponseServerError(status=403)


def user_logout(request):
    print("loguout")
    logout(request)
    return HttpResponseRedirect("/")


def delete_user(request):
    user_id = request.POST.get("user_id", "")
    User.objects.filter(id=user_id).delete()
    return HttpResponse("200")