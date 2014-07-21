from django.contrib import admin

# Register your models here.

from game.models import Pokemon, Team

admin.site.register(Pokemon)
admin.site.register(Team)