import json
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from game.models import ScoreKeeping


def home(request):
	return render(request, 'index.html')


def login(request):
	return render(request, 'registration/login.html')


def logout(request):
	"""Logs out user"""
	return render(request, 'registration/logout.html')


def game(request):
	return render(request, 'game.html')


def leaderboard(request):
	return render(request, 'leaderboard.html')


def score_return(request):
	lead_score = ScoreKeeping.objects.all()
	collection = []
	for score in lead_score:
		collection.append({
			'game_name': score.choice_of_game,
			'high_score': score.high_score,
			'username': score.user_id,
			'date': score.time

		})
	return HttpResponse(json.dumps(collection, cls=DjangoJSONEncoder),
	                    content_type='application.json')