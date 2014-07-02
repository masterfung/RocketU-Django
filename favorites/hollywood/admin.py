from django.contrib import admin
from hollywood.models import Actor, Genre, Movie

# Register your models here.

class MovieAdmin(admin.ModelAdmin):
	list_display = ('name', 'release_year', 'length', 'imdb', 'genre')

class ActorAdmin(admin.ModelAdmin):
	list_display = ('name', 'age')



admin.site.register(Actor, ActorAdmin)
admin.site.register(Genre)
admin.site.register(Movie, MovieAdmin)