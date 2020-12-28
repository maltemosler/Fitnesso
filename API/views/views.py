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
            goal_percent = 0
            for unterziel in Unterziel.objects.filter(hauptziel=hauptziel):
                unterziele.append({"id": unterziel.id, "ziel": unterziel.ziel, "status": unterziel.status})
            if not hauptziel.id in ziele:
                all_goals = Unterziel.objects.filter(hauptziel=hauptziel, status=True).count()
                all_goals_done = Unterziel.objects.filter(hauptziel=hauptziel).count()

                if all_goals != 0 and all_goals_done != 0:
                    goal_percent = (all_goals / all_goals_done) * 100

                ziele.append(
                    {"id": hauptziel.id, "ziel": hauptziel.ziel, "unterziele": unterziele,
                     "status": goal_percent
                     }
                )

    context["ziele"] = ziele
    return render(request, "ziele.html", context=global_context(request, context))


def reset_passwort_view(request, user_id):
    context = {'title': "Fitnesso | Ziele"}
    if request.user.is_authenticated:
        if request.user.fitnessouser.is_trainer:
            user = FitnessoUser.objects.get(user_id=user_id)
            context["vorname"] = user.vorname
            context["nachname"] = user.nachname

    return render(request, "reset_passwort.html", context=global_context(request, context))


def user_anlegen_view(request):
    context = {'title': "Fitnesso | User anlegen"}
    return render(request, "user_anlegen.html", context=global_context(request, context))


def tests(request):
    context = {'title': "Fitnesso | Tests"}
    return render(request, "tests.html", context=global_context(request, context))
