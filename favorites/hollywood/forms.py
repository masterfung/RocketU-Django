from django.forms import ModelForm
from hollywood.models import Genre, Movie

__author__ = '@masterfung'


class GenreForm(ModelForm):
    class Meta:
        model = Genre

class MovieForm(ModelForm):
    class Meta:
        model = Movie