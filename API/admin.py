from django.contrib import admin

# Register your models here.
from API.models import HauptZiel, FitnessoUser, Unterziel#, TrainerAssoc

# admin.site.register(TrainerAssoc)
admin.site.register(FitnessoUser)
admin.site.register(HauptZiel)
admin.site.register(Unterziel)