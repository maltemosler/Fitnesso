from django.shortcuts import render


# Create your views here.
def home_view(request):
    context = {'title': "Fitnesso"}
    return render(request, "home.html", context=context)
