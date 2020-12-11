from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponseServerError, HttpResponse
from django.shortcuts import render

from API.models import FitnessoUser, HauptZiel, Unterziel
from API.tasks import validations


def global_context(request, context):
    return context


def home_view(request):
    context = {'title': "Fitnesso | Home"}
    if request.user.is_authenticated:
        if request.user.fitnessouser.is_trainer:
            context["users"] = FitnessoUser.objects.filter()
        else:
            ziele = []
            for hauptziel in HauptZiel.objects.filter():
                unterziele = []
                for unterziel in Unterziel.objects.filter(hauptziel=hauptziel):
                    unterziele.append({"id": unterziel.id, "ziel": unterziel.ziel})
                if not hauptziel.id in ziele:
                    ziele.append({"id": hauptziel.id, "ziel": hauptziel.ziel, "unterziele": unterziele})

            context["ziele"] = ziele
    return render(request, "home.html", context=global_context(request, context))


# @only_ajax
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
        return HttpResponse()
    else:
        return HttpResponseServerError(status=403)


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


def delete_user(request):
    user_id = request.POST.get("user_id", "")
    User.objects.filter(id=user_id).delete()
    return HttpResponse("200")


def user_anlegen_view(request):
    context = {'title': "Fitnesso | User anlegen"}
    return render(request, "user_anlegen.html", context=global_context(request, context))


def tests(request):
    context = {'title': "Fitnesso | Tests"}
    return render(request, "tests.html", context=global_context(request, context))