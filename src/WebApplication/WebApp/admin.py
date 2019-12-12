from django.contrib import admin

# Register your models here.

from .models import BlacklistDB, MininglistDB

admin.site.register(BlacklistDB)
admin.site.register(MininglistDB)