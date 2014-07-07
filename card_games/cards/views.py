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