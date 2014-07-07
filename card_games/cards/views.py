from django.shortcuts import render
from cards.models import Card

# Create your views here.



def home(request):
	data = {
		'cards': Card.objects.all()
	}

	return render(request, 'cards.html', data)


def clubs(request):
	data = {
		'clubs': Card.objects.all()
	}

	return render(request, 'clubs.html', data)


def diamonds_hearts(request):
	data = {
		'choices': Card.objects.all()
	}

	return render(request, 'diamonds_heart.html', data)

def spades(request):
	data = {
		'spades': Card.objects.all()
	}

	return render(request, 'spades.html', data)

def faces(request):
	data = {
		'faces': Card.objects.all()
	}

	return render(request, 'face.html', data)

def cards_filters(request):
	data = {
		'cards': Card.objects.all()
	}

	return render(request, 'cards_filters.html', data)