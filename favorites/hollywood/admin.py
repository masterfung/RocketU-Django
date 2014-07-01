from django.contrib import admin
from hollywood.models import Actor, Genre, Movie

# Register your models here.

admin.site.register(Actor)
admin.site.register(Genre)
admin.site.register(Movie)