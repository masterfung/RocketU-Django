from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from hollywood.models import Actor, Genre, Movie, Video

# Register your models here.

class MovieAdmin(admin.ModelAdmin):
	list_display = ('name', 'release_year', 'length', 'imdb', 'genre')

	list_filter = ['name']
	search_fields = ['name']

class ActorAdmin(admin.ModelAdmin):
	list_display = ('name', 'age')

class VideoAdmin(AdminVideoMixin, admin.ModelAdmin):
	pass

admin.site.register(Actor, ActorAdmin)
admin.site.register(Genre)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Video, VideoAdmin)