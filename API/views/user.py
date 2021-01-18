from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from django.db import transaction
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseServerError, JsonResponse
from django.views.decorators.http import require_http_methods

from API.models import FitnessoUser
from API.tasks import validations


# Prevent errors caused by wrong request method
# transaction to prevent corrupted database
@require_http_methods(["POST"])
@transaction.atomic
def register(request):
    # get email from post request
    email = request.POST.get("email", "").lower()
    if not validations.validate_email(email):
        return HttpResponseServerError("422-0")
    # get password from post request
    password = request.POST.get("password", "")
    if not validations.validate_password(password):
        return HttpResponseServerError("422-1")
    # get vorname from post request
    vorname = request.POST.get("vorname", "")
    if not validations.validate_first_name(vorname):
        return HttpResponseServerError("422-2")
    # get nachname from post request
    nachname = request.POST.get("nachname", "")
    if not validations.validate_last_name(nachname):
        return HttpResponseServerError("422-3")

    # try to create a new user when this email doesn't exists
    user, new = User.objects.get_or_create(username=email)
    if not new:
        print("user not new")
        return HttpResponseServerError("409")

    # set email from user
    user.email = email
    # set password from user
    user.set_password(password)
    # update database
    user.save()

    # create Fitnesso User (erbt von user)
    su = FitnessoUser.objects.create(user=user)
    # set vorname
    su.vorname = vorname
    # set nachname
    su.nachname = nachname
    su.save()

    return HttpResponse("200")


# Prevent errors caused by wrong request method
# transaction to prevent corrupted database
@require_http_methods(["POST"])
@transaction.atomic
def user_login(request):
    # get email from post request
    email = request.POST.get("email", "").lower()
    if not validations.validate_email(email):
        return HttpResponseServerError(status=422)

    # get password from post request
    password = request.POST.get("password", "")
    if not validations.validate_password(password):
        return HttpResponseServerError(status=422)

    # check if Email exists in Database
    try:
        user = User.objects.get(username=email)
    except User.DoesNotExist:
        return HttpResponse(status=403)

    su, new = FitnessoUser.objects.get_or_create(user=user)

    # try to authenticate user
    try:
        user = authenticate(request, username=email, password=password)
    except:
        return HttpResponseServerError(status=403)

    if user is not None and su:
        # if authenticate was successfully then login the users
        login(request, user)
        # return json response with boolean is_trainer to know where to redirect the user
        return JsonResponse({"is_trainer": su.is_trainer, "user_id": su.user.id})
    else:
        return HttpResponseServerError(status=403)


# method to logout the user
def user_logout(request):
    logout(request)
    return HttpResponseRedirect("/")


# Prevent errors caused by wrong request method
# transaction to prevent corrupted database
@require_http_methods(["POST"])
@transaction.atomic
def reset_password(request):
    # get user id from post request
    user_id = request.POST.get("user_id", None)
    if not user_id:
        return HttpResponseServerError("user_id id missing")
    # get new passwort from post request
    new_password = request.POST.get("new_password", None)
    if not new_password:
        return HttpResponseServerError("new_password missing")

    if request.user.is_authenticated:
        if request.user.fitnessouser.is_trainer:
            # get user from database
            user = User.objects.get(id=user_id)
            # set password
            user.set_password(new_password)
            # update database
            user.save()

            return HttpResponse("200")
        return HttpResponse("403")
    return HttpResponse("403")


# Prevent errors caused by wrong request method
# transaction to prevent corrupted database
@require_http_methods(["POST"])
@transaction.atomic
def delete_user(request):
    # get user id from post request
    user_id = request.POST.get("user_id", "")

    # check if user is not the user who requested this (prevent deletion of trainer himself)
    if str(user_id) != str(request.user.id):
        # filter for the user with the right id and delete
        User.objects.filter(id=user_id).delete()
    return HttpResponse("200")
