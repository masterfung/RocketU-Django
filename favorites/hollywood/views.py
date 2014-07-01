from django.shortcuts import render, render_to_response, redirect
from hollywood.models import Genre
from hollywood.forms import GenreForm

# Create your views here.

def home(request):
	return render(request, "home.html")


def genres(request):
	genres = Genre.objects.all()
	return render_to_response("genres.html", {'genres': genres})


def new_genre(request):
	# If the user is submitting the form
	if request.method == "POST":

		# Get the instance of the form filled with the submitted data
		form = GenreForm(request.POST)

		# Django will check the form's validity for you
		if form.is_valid():

			# Saving the form will create a new Genre object
			if form.save():
				# After saving, redirect the user back to the index page
				return redirect("/genres")

	# Else if the user is looking at the form page
	else:
		form = GenreForm()
	data = {'form': form}
	return render(request, "new_genre.html", data)