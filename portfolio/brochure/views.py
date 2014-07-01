from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello(request, name):
	return HttpResponse("Hello, {}".format(name))


def justice(request):
	return HttpResponse('Welcome to the world of Justice! Justice League. Assembled!!')


def variable(request, name):
	return HttpResponse("I love {}".format(name))


def fizzbuzz(request, first, second):
	fizzbuzz = []
	if int(first) % 3 == 0:
		fizzbuzz.append('fizz')
	if int(second) % 5 == 0:
		fizzbuzz.append('buzz')
	return HttpResponse(fizzbuzz)