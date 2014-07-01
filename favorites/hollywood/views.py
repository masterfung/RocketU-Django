from django.shortcuts import render, render_to_response
from hollywood.models import Genre

# Create your views here.

def home(request):
    return render(request, "home.html"),

def genres(request):
    genres = Genre.objects.all()
    return render_to_response("genres.html", {'genres': genres})