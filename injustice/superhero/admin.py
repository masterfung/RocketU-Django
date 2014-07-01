from django.contrib import admin
from superhero.models import Player, Team, Location, Power, Alliance

# Register your models here.

class PlayerAdmin(admin.ModelAdmin):
	list_display = ('superhero_name', 'real_name', 'type', 'age', 'location', 'affiliation')

class TeamAdmin(admin.ModelAdmin):
	list_display = ('name', 'alliance')


class PowerAdmin(admin.ModelAdmin):
	list_display = ('power', 'good_bad')


admin.site.register(Player, PlayerAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Location)
admin.site.register(Alliance)
admin.site.register(Power, PowerAdmin)