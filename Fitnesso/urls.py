"""Fitnesso URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')ssword:
•••••••

Nutzer anlegen
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path

from API.views.user import register, user_login, delete_user, user_logout
from API.views.views import home_view, tests, user_anlegen_view, ziele_view, user_verwaltung
from API.views.ziele import hauptziel_erstellen, hauptziel_delete, unterziel_erstellen, unterziel_abschliessen, \
    unterziel_delete

urlpatterns = [
    path('', home_view),

    path('user_verwaltung/', user_verwaltung),
    path('user_anlegen/', user_anlegen_view),
    path('register/', register),
    path('ziele/<user_id>', ziele_view),

    path('ajax/user_login/', user_login),
    path('ajax/register/', register),
    path('ajax/delete_user/', delete_user),

    path('ajax/hauptziel_erstellen/', hauptziel_erstellen),
    path('ajax/hauptziel_delete/', hauptziel_delete),

    path('ajax/unterziel_erstellen/', unterziel_erstellen),
    path('ajax/unterziel_abschliessen/', unterziel_abschliessen),
    path('ajax/unterziel_delete/', unterziel_delete),

    path('tests', tests),
    path('admin/', admin.site.urls),
    path('user_logout', user_logout, name="user_logout"),
]
