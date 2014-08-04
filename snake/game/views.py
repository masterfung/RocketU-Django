from django.shortcuts import render

# Create your views here.

def home(request):
	return render(request, 'base.html')

def login(request):
	return render(request, 'registration/login.html')

def logout(request):
	"""Logs out user"""
	return render(request, 'registration/logout.html')

def game(request):
	return render(request, 'game.html')

def leaderboard(request):
	return render(request, 'leaderboard.html')