from brochure.forms import ContactForm
from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse

# Create your views here.
from brochure.models import Contact


def hello(request):
	return render_to_response("index.html")

def portfolio(request):
	return render_to_response('portfolio.html')

# def contact(request):
# 	return render_to_response('contact.html')

def about(request):
	return render_to_response('about.html')

def entrepreneur(request):
	return render_to_response('entrepreneur.html')

def hacker(request):
	return render_to_response('hacker.html')

def artist(request):
	return render_to_response('artist.html')

def art(request):
	return render_to_response('art.html')

def code(request):
	return render_to_response('code.html')

# def contact(request):
# 	data = {"contact_form": ContactForm()}
# 	return render(request, "contact.html", data)

def new_contact(request):
	# If the user is submitting the form
	if request.method == "POST":

		# Get the instance of the form filled with the submitted data
		form = ContactForm(request.POST)

		# Django will check the form's validity for you
		if form.is_valid():

			# Saving the form will create a new Genre object
			if form.save():
				# After saving, redirect the user back to the index page
				return redirect("/")

	# Else if the user is looking at the form page
	else:
		form = ContactForm()
	data = {'form': form}
	return render(request, "contact.html", data)

def fizzbuzz(request, first, second):
	fizzbuzz = []
	if int(first) % 3 == 0:
		fizzbuzz.append('fizz')
	if int(second) % 5 == 0:
		fizzbuzz.append('buzz')
	return HttpResponse(fizzbuzz)