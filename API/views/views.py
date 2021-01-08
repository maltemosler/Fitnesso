from django.shortcuts import render
from API.models import FitnessoUser, HauptZiel, Unterziel


# default redirect view / login View
def home_view(request):
    context = {'title': "Login"}
    return render(request, "home.html", context=context)


# shows the user verwaltung
def user_verwaltung(request):
    context = {'title': "User Verwaltung"}
    # check if user is logged in
    if request.user.is_authenticated:
        # check if you are trainer
        if request.user.fitnessouser.is_trainer:
            # get all users
            context["users"] = FitnessoUser.objects.filter()

            # calculate total goals percentage
            # Hier wird durch alle Unterziele iteriert und geschaut, ob das Ziel abgeschlossen ist, oder nicht.
            # So kann ausgerechnet werden, wie viel % ein user bereits hat.
            i = 0
            for user in context["users"]:
                j = 0
                goal_reached = 0
                for unterziel in Unterziel.objects.filter(hauptziel__user=user):
                    j += 1

                    if unterziel.status:
                        goal_reached += 1

                # update users total_goal_percentage
                if goal_reached != 0:
                    context["users"][i].total_goal_percentage = int(goal_reached / j * 100)
                else:
                    context["users"][i].total_goal_percentage = 0
                i += 1

    return render(request, "user_verwaltung.html", context=context)


# die view für ziele, kann vom Nutzer und Trainer aufgerufen werden
def ziele_view(request, user_id):
    ziele = []
    context = {'title': "Ziele"}
    # check if user is authenticated
    if request.user.is_authenticated:
        # get user (get from request when not trainer or get user_id when trainer)
        if request.user.fitnessouser.is_trainer:
            user = FitnessoUser.objects.filter(user_id=user_id).first()
        else:
            user = FitnessoUser.objects.filter(user=request.user.fitnessouser).first()

        if user:
            hauptziele = HauptZiel.objects.filter(user=user)

            # get vorname und nachname from user (will displayed in ziele.html)
            context["vorname"] = user.vorname
            context["nachname"] = user.nachname

            for hauptziel in hauptziele:
                unterziele = []
                goal_percent = 0
                # füge alle unterziele zum hauptziel hinzu
                for unterziel in Unterziel.objects.filter(hauptziel=hauptziel):
                    unterziele.append({"id": unterziel.id, "ziel": unterziel.ziel, "status": unterziel.status})

                if not hauptziel.id in ziele:
                    # calculate percentage done in ziele
                    all_goals = Unterziel.objects.filter(hauptziel=hauptziel, status=True).count()
                    all_goals_done = Unterziel.objects.filter(hauptziel=hauptziel).count()

                    if all_goals != 0 and all_goals_done != 0:
                        goal_percent = int((all_goals / all_goals_done) * 100)

                    # füge hauptziel mit den unterzielen hinzu
                    ziele.append(
                        {"id": hauptziel.id, "ziel": hauptziel.ziel, "unterziele": unterziele,
                         "status": goal_percent
                         }
                    )

    context["ziele"] = ziele
    return render(request, "ziele.html", context=context)


# view um das passwort zu resetten. Nimmt als parameter die user_id an um zu wissen, um welchen Nutzer es sich handelt.
def reset_passwort_view(request, user_id):
    context = {'title': "Reset Passwort"}
    # Antragsteller eingeloggt?
    if request.user.is_authenticated:
        # Ist der Antragsteller Trainer?
        if request.user.fitnessouser.is_trainer:
            user = FitnessoUser.objects.get(user_id=user_id)
            context["vorname"] = user.vorname
            context["nachname"] = user.nachname

    return render(request, "reset_passwort.html", context=context)


# view für die user anlegen seite. Gibt die HTML Webseite mit passender Überschrift zurück
def user_anlegen_view(request):
    context = {'title': "User anlegen"}
    return render(request, "user_anlegen.html", context=context)


# view für alle unit-tests
def tests(request, user_id):
    context = {'title': "Tests"}
    return render(request, "tests.html", context=context)
