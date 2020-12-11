from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponseServerError, HttpResponse
from django.shortcuts import render

from API.models import FitnessoUser, HauptZiel, Unterziel
from API.tasks import validations
from Fitnesso.decorators import only_ajax


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


def user_anlegen_view(request):
    context = {'title': "Fitnesso | User anlegen"}
    return render(request, "user_anlegen.html", context=global_context(request, context))


def user_verwalten_view(request):
    context = {'title': "Fitnesso | User verwalten"}
    return render(request, "user_verwalten.html", context=global_context(request, context))


def tests(request):
    context = {'title': "Fitnesso | Tests"}
    return render(request, "tests.html", context=global_context(request, context))