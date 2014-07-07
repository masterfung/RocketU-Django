from django.forms import ModelForm
from hollywood.models import Genre, Movie, Actor, Video

__author__ = '@masterfung'


class GenreForm(ModelForm):
	class Meta:
		model = Genre


class MovieForm(ModelForm):
	class Meta:
		model = Movie


class ActorForm(ModelForm):
	class Meta:
		model = Actor


class VideoForm(ModelForm):
	class Meta:
		model = Video