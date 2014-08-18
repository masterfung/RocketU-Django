from django.shortcuts import render

# Create your views here.

def home(request):
	return render(request, 'base.html')

def angular(request):
	return render(request, 'angular.html')