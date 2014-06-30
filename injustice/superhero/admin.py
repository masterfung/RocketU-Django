from django.contrib import admin
from superhero.models import Player, Team, Location, Power

# Register your models here.

admin.site.register(Player)
admin.site.register(Team)
admin.site.register(Location)
admin.site.register(Power)