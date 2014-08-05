import json
from django.contrib.auth.decorators import login_required
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse
from django.shortcuts import render, render_to_response


# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from game.models import ScoreKeeping


def home(request):
	return render(request, 'index.html')


def login(request):
	return render(request, 'registration/login.html')


def logout(request):
	"""Logs out user"""
	return render(request, 'registration/logout.html')

@login_required
def game(request):
	return render(request, 'game.html')


# def leaderboard(request):
# 	return render(request, 'leaderboard.html')

@login_required
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


@csrf_exempt
def leaderboard_snake(request):
	snake = {}
	if request.method == 'POST':
		data = json.loads(request.body)
		score = ScoreKeeping.objects.create(
			user=request.user,
			high_score=data['high_score'],
			choice_of_game=data['choice_of_game'],

		)
		snake = {
			'choice_of_game': score.choice_of_game,
			'high_score': score.high_score,
			'user': score.user_id,
			'time': score.time
		}
	return HttpResponse(json.dumps(snake, cls=DjangoJSONEncoder),
	                    content_type='application.json')


def user_scores(request):
	lead_score = ScoreKeeping.objects.all().order_by('-high_score')
	return render(request, 'leaderboard.html', {'lead_score': lead_score})