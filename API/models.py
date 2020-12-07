from django.db import models


class Trainer(models.Model):
    vorname = models.CharField(max_length=32, null=True)
    nachname = models.CharField(max_length=32, null=True)


class FitnessoUser(models.Model):
    trainer = models.ForeignKey(Trainer, models.CASCADE, null=True)
    vorname = models.CharField(max_length=32, null=True)
    nachname = models.CharField(max_length=32, null=True)


class HauptZiel(models.Model):
    user = models.ForeignKey(FitnessoUser, models.CASCADE, null=True)
    ziel = models.CharField(max_length=256, null=True)
    status = models.BooleanField(default=True, null=False)


class Unterziel(models.Model):
    hauptziel = models.ForeignKey(HauptZiel, models.CASCADE, null=True)
    ziel = models.CharField(max_length=128, null=True)
    status = models.BooleanField(default=True, null=False)