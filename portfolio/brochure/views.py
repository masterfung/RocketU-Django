from django.shortcuts import render, render_to_response
from django.http import HttpResponse

# Create your views here.

def hello(request):
	return render_to_response("index.html")

def portfolio(request):
	return render_to_response('portfolio.html')

def contact(request):
	return render_to_response('contact.html')


def fizzbuzz(request, first, second):
	fizzbuzz = []
	if int(first) % 3 == 0:
		fizzbuzz.append('fizz')
	if int(second) % 5 == 0:
		fizzbuzz.append('buzz')
	return HttpResponse(fizzbuzz)