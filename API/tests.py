from django.contrib.auth.models import User
from django.test import TestCase, Client

from API.models import FitnessoUser, Unterziel, HauptZiel


class TestBackend(TestCase):

    def setUp(self):
        user = User.objects.create(username="admin@admin.de")
        user.set_password('12345')
        user.save()
        FitnessoUser.objects.create(
            user=user,
            vorname="adminvorname",
            nachname="adminnachname",
            is_trainer=True
        )

        user = User.objects.create(username="user@user.de")
        user.set_password('12345')
        user.save()
        fu = FitnessoUser.objects.create(
            user=user,
            vorname="uservorname",
            nachname="nutzernachname",
            is_trainer=False
        )
        ziel = HauptZiel.objects.create(user=fu, ziel="hauptziel dinge tun")
        Unterziel.objects.create(hauptziel=ziel, ziel="dinge tun")

    def test_hauptziel(self):
        c = Client()
        l = c.login(username="user@user.de", password="12345")

        user_id = FitnessoUser.objects.filter(is_trainer=False).first().user.id

        resp = c.post("/ajax/hauptziel_erstellen/", {"user_id": user_id, "ziel": "Joga"})
        self.assertEqual(resp.status_code, 200)

    def test_hauptziel_no_goal(self):
        c = Client()
        l = c.login(username="user@user.de", password="12345")

        user_id = FitnessoUser.objects.filter(is_trainer=False).first().user.id

        resp = c.post("/ajax/hauptziel_erstellen/", {"user_id": user_id})
        self.assertEqual(resp.status_code, 500)

    def test_hauptziel_delete(self):
        c = Client()
        l = c.login(username="user@user.de", password="12345")

        user_id = FitnessoUser.objects.filter(is_trainer=False).first().user.id

        resp = c.post("/ajax/hauptziel_delete/", {"user_id": user_id, "ziel_id": HauptZiel.objects.first().id})
        self.assertEqual(resp.status_code, 200)

    def test_hauptziel_delete_fail(self):
        c = Client()
        l = c.login(username="user@user.de", password="12345")

        user_id = FitnessoUser.objects.filter(is_trainer=False).first().user.id

        resp = c.post("/ajax/hauptziel_delete/", {"user_id": user_id})
        self.assertEqual(resp.status_code, 500)

    def test_unterziel_erstellen(self):
        c = Client()
        l = c.login(username="user@user.de", password="12345")

        user_id = FitnessoUser.objects.filter(is_trainer=False).first().user.id

        resp = c.post("/ajax/unterziel_erstellen/", {"user_id": user_id, "hauptziel_id": HauptZiel.objects.first().id, "ziel": "nix"})
        self.assertEqual(resp.status_code, 200)

    def test_unterziel_erstellen_fail(self):
        c = Client()
        l = c.login(username="user@user.de", password="12345")

        user_id = FitnessoUser.objects.filter(is_trainer=False).first().user.id

        resp = c.post("/ajax/unterziel_erstellen/", {"user_id": user_id})
        self.assertEqual(resp.status_code, 500)

    def test_unterziel_abschliessen(self):
        c = Client()
        l = c.login(username="user@user.de", password="12345")

        user_id = FitnessoUser.objects.filter(is_trainer=False).first().user.id

        resp = c.post("/ajax/unterziel_abschliessen/", {"user_id": user_id, "unterziel_id": Unterziel.objects.first().id})
        self.assertEqual(resp.status_code, 200)

    def test_unterziel_abschliessen_fail(self):
        c = Client()
        l = c.login(username="user@user.de", password="12345")

        user_id = FitnessoUser.objects.filter(is_trainer=False).first().user.id

        resp = c.post("/ajax/unterziel_abschliessen/", {"user_id": user_id})
        self.assertEqual(resp.status_code, 500)

    def test_unterziel_delete(self):
        c = Client()
        l = c.login(username="user@user.de", password="12345")

        user_id = FitnessoUser.objects.filter(is_trainer=False).first().user.id

        resp = c.post("/ajax/unterziel_delete/", {"user_id": user_id, "unterziel_id": Unterziel.objects.first().id})
        self.assertEqual(resp.status_code, 200)

    def test_unterziel_delete_fail(self):
        c = Client()
        l = c.login(username="user@user.de", password="12345")

        user_id = FitnessoUser.objects.filter(is_trainer=False).first().user.id

        resp = c.post("/ajax/unterziel_delete/", {"user_id": user_id})
        self.assertEqual(resp.status_code, 500)

    def test_reset_password(self):
        c = Client()
        l = c.login(username="user@user.de", password="12345")

        user_id = FitnessoUser.objects.filter(is_trainer=False).first().user.id

        resp = c.post("/ajax/reset_password/", {"user_id": user_id, "new_password": "13378482143"})
        self.assertEqual(resp.status_code, 200)

    def test_reset_password_fail(self):
        c = Client()
        l = c.login(username="user@user.de", password="12345")

        user_id = FitnessoUser.objects.filter(is_trainer=False).first().user.id

        resp = c.post("/ajax/reset_password/", {"user_id": user_id})
        self.assertEqual(resp.status_code, 500)
