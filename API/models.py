from django.contrib.auth.models import User
from django.db import models


class FitnessoUser(models.Model):
    user = models.OneToOneField(User, models.CASCADE, primary_key=True)  # need because of auth backend.
    vorname = models.CharField(max_length=32, null=True)
    nachname = models.CharField(max_length=32, null=True)
    password = models.CharField(max_length=64, null=True)
    is_trainer = models.BooleanField(default=False, null=False)
    # trainer = models.ForeignKey(User, models.CASCADE)

    def __str__(self):
        return "{}".format(self.nachname)


# todo: user trainer assoc

class HauptZiel(models.Model):
    user = models.ForeignKey(FitnessoUser, models.CASCADE, null=True)
    ziel = models.CharField(max_length=256, null=True)
    status = models.BooleanField(default=False, null=False)

    def __str__(self):
        return "{}".format(self.ziel)


class Unterziel(models.Model):
    hauptziel = models.ForeignKey(HauptZiel, models.CASCADE, null=True)
    ziel = models.CharField(max_length=128, null=True)
    status = models.BooleanField(default=False, null=False)

    def __str__(self):
        return "{}".format(self.ziel)