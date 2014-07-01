from django.forms import ModelForm
from hollywood.models import Genre

__author__ = '@masterfung'


class GenreForm(ModelForm):
    class Meta:
        model = Genre