from django.shortcuts import render

from API.models import FitnessoUser, HauptZiel, Unterziel


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


def user_anlegen_view(request):
    context = {'title': "Fitnesso | User anlegen"}
    return render(request, "user_anlegen.html", context=global_context(request, context))


def user_verwalten_view(request):
    context = {'title': "Fitnesso | User verwalten"}
    return render(request, "user_verwalten.html", context=global_context(request, context))


def tests(request):
    context = {'title': "Fitnesso | Tests"}
    return render(request, "tests.html", context=global_context(request, context))