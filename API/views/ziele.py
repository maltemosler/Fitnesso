from django.contrib.auth.models import User
from django.db import transaction
from django.http import HttpResponseServerError, HttpResponse
from django.views.decorators.http import require_http_methods

from API.models import Unterziel, HauptZiel
from Fitnesso.decorators import validate_goal_user_rights


# Prevent errors caused by wrong request method
# transaction to prevent corrupted database
@require_http_methods(["POST"])
@transaction.atomic
@validate_goal_user_rights
def hauptziel_erstellen(request):
    # get user id from post request
    user_id = request.POST.get("user_id", None)
    if not user_id:
        return HttpResponseServerError("user_id missing")
    # get ziel (string) from post request
    ziel = request.POST.get("ziel", None)
    if not ziel:
        return HttpResponseServerError("ziel missing")

    try:
        HauptZiel.objects.create(user_id=user_id, ziel=ziel)
    except:
        return HttpResponseServerError("user id does not exist")

    return HttpResponse("200")


# Prevent errors caused by wrong request method
# transaction to prevent corrupted database
@require_http_methods(["POST"])
@transaction.atomic
@validate_goal_user_rights
def hauptziel_delete(request):
    # get user id from post request
    user_id = request.POST.get("user_id", None)
    if not user_id:
        return HttpResponseServerError("user id missing")
    # get ziel (string) from post request
    ziel_id = request.POST.get("ziel_id", None)
    if not ziel_id:
        return HttpResponseServerError("ziel id missing")

    try:
        z = HauptZiel.objects.get(user_id=user_id, id=ziel_id)
    except HauptZiel.DoesNotExist:
        return HttpResponseServerError("Ziel doesn't exists")
    z.delete()
    return HttpResponse("200")


# Prevent errors caused by wrong request method
# transaction to prevent corrupted database
@require_http_methods(["POST"])
@transaction.atomic
@validate_goal_user_rights
def unterziel_erstellen(request):
    # get user id from post request
    user_id = request.POST.get("user_id", None)
    if not user_id:
        return HttpResponseServerError("user_id missing")
    # get ziel (string) from post request
    ziel = request.POST.get("ziel", None)
    if not ziel:
        return HttpResponseServerError("ziel missing")
    # get hauptziel id from post request
    hauptziel_id = request.POST.get("hauptziel_id", None)
    if not hauptziel_id:
        return HttpResponseServerError("hauptziel id missing")

    # get hauptziel
    try:
        hauptziel = HauptZiel.objects.get(id=hauptziel_id, user_id=user_id)
    except HauptZiel.DoesNotExist:
        return HttpResponseServerError("hauptziel does not exist")

    # create unterziel
    Unterziel.objects.create(hauptziel=hauptziel, ziel=ziel)

    return HttpResponse("200")


# Prevent errors caused by wrong request method
# transaction to prevent corrupted database
@require_http_methods(["POST"])
@transaction.atomic
@validate_goal_user_rights
def unterziel_abschliessen(request):
    # get user id from post request
    user_id = request.POST.get("user_id", None)
    if not user_id:
        return HttpResponseServerError("user_id missing")
    # get unterziel id from post request
    unterziel_id = request.POST.get("unterziel_id", None)
    if not unterziel_id:
        return HttpResponseServerError("unterziel id missing")

    try:
        uz = Unterziel.objects.get(id=unterziel_id)
    except Unterziel.DoesNotExist:
        return HttpResponseServerError("can't find unterziel")

    # check if user from hauptziel is user who requested this change,
    if int(uz.hauptziel.user.user_id) == int(user_id) or request.user.fitnessouser.is_trainer:
        uz.status = True
        uz.save()
    return HttpResponse("200")


# Prevent errors caused by wrong request method
# transaction to prevent corrupted database
@require_http_methods(["POST"])
@transaction.atomic
@validate_goal_user_rights
def unterziel_delete(request):
    # get user id from post request
    user_id = request.POST.get("user_id", None)
    if not user_id:
        return HttpResponseServerError("user_id missing")
    # get unterziel id from post request
    unterziel_id = request.POST.get("unterziel_id", None)
    if not unterziel_id:
        return HttpResponseServerError("unterziel id missing")

    try:
        uz = Unterziel.objects.get(id=unterziel_id)
    except Unterziel.DoesNotExist:
        return HttpResponseServerError("can't find unterziel")

    # check if user from hauptziel is user who requested this change
    if int(uz.hauptziel.user.user_id) == int(user_id) or request.user.fitnessouser.is_trainer:
        uz.delete()
    return HttpResponse("200")
