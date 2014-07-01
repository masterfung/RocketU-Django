from django.contrib import admin
from gameplay.models import Type, Level, Pokemon, Trainer, Power, Boss

# Register your models here.

class TrainerAdmin(admin.ModelAdmin):
	list_display = ('name', 'age', 'gender', 'level')


class PokemonAdmin(admin.ModelAdmin):
	list_display = ('name', 'attack', 'health', 'type', 'power')

class BossAdmin(admin.ModelAdmin):
	list_display = ('name', 'age', 'gender', 'region', 'difficulty')

admin.site.register(Type)
admin.site.register(Level)
admin.site.register(Pokemon)
admin.site.register(Trainer, TrainerAdmin)
admin.site.register(Power)
admin.site.register(Boss, BossAdmin)
