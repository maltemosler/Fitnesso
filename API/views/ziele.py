from django.http import HttpResponseServerError, HttpResponse

from API.models import Unterziel, HauptZiel
from Fitnesso.decorators import validate_user


@validate_user
def hauptziel_erstellen(request):
    user_id = request.POST.get("user_id", "")
    ziel = request.POST.get("ziel", "")

    HauptZiel.objects.create(user_id=user_id, ziel=ziel)

    return HttpResponse("200")


@validate_user
def hauptziel_delete(request):
    user_id = request.POST.get("user_id", "")
    ziel_id = request.POST.get("ziel_id", "")

    HauptZiel.objects.filter(user_id=user_id, id=ziel_id).delete()
    return HttpResponse("200")


@validate_user
def unterziel_erstellen(request):
    user_id = request.POST.get("user_id", "")
    ziel = request.POST.get("ziel", "")
    hauptziel_id = request.POST.get("hauptziel_id", "")

    hauptziel = HauptZiel.objects.get(id=hauptziel_id, user_id=user_id)
    Unterziel.objects.create(hauptziel=hauptziel, ziel=ziel)
    return HttpResponse("200")


@validate_user
def unterziel_abschliessen(request):
    user_id = request.POST.get("user_id", "")
    unterziel_id = request.POST.get("unterziel_id", "")

    uz = Unterziel.objects.get(id=unterziel_id)

    # check if user from hauptziel is user who requested this change,
    if int(uz.hauptziel.user.user_id) == int(user_id) or request.user.fitnessouser.is_trainer:
        uz.status = True
        uz.save()
    return HttpResponse("200")


@validate_user
def unterziel_delete(request):
    user_id = request.POST.get("user_id", "")
    unterziel_id = request.POST.get("unterziel_id", "")

    uz = Unterziel.objects.get(id=unterziel_id)

    # check if user from hauptziel is user who requested this change
    if int(uz.hauptziel.user.user_id) == int(user_id) or request.user.fitnessouser.is_trainer:
        uz.delete()
    return HttpResponse("200")
