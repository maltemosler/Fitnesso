from django.shortcuts import render
from API.models import FitnessoUser, HauptZiel, Unterziel


def global_context(request, context):
    return context


def home_view(request):
    context = {'title': "Fitnesso | Home"}

    return render(request, "home.html", context=global_context(request, context))


def user_verwaltung(request):
    context = {'title': "Fitnesso | Home"}
    if request.user.is_authenticated:
        if request.user.fitnessouser.is_trainer:
            context["users"] = FitnessoUser.objects.filter()
    return render(request, "user_verwaltung.html", context=global_context(request, context))


def ziele_view(request, user_id):
    ziele = []
    context = {'title': "Fitnesso | Ziele"}
    if request.user.is_authenticated:
        if request.user.fitnessouser.is_trainer:
            hauptziele = HauptZiel.objects.filter(user_id=user_id)
        else:
            hauptziele = HauptZiel.objects.filter(user=request.user.fitnessouser)

        for hauptziel in hauptziele:
            unterziele = []
            for unterziel in Unterziel.objects.filter(hauptziel=hauptziel):
                unterziele.append({"id": unterziel.id, "ziel": unterziel.ziel, "status": unterziel.status})
            if not hauptziel.id in ziele:
                ziele.append(
                    {"id": hauptziel.id, "ziel": hauptziel.ziel, "unterziele": unterziele,
                     "status": f"{Unterziel.objects.filter(hauptziel=hauptziel, status=True).count()}/{Unterziel.objects.filter(hauptziel=hauptziel).count()}"
                     }
                )

    context["ziele"] = ziele
    return render(request, "ziele.html", context=global_context(request, context))


def user_anlegen_view(request):
    context = {'title': "Fitnesso | User anlegen"}
    return render(request, "user_anlegen.html", context=global_context(request, context))


def tests(request):
    context = {'title': "Fitnesso | Tests"}
    return render(request, "tests.html", context=global_context(request, context))
