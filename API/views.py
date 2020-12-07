from django.shortcuts import render


def global_context(request, context):
    return context


def home_view(request):
    context = {'title': "Fitnesso | Home"}
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