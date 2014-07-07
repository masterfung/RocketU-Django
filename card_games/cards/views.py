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


def tags(request):
    data = {
        'cards': Card.objects.all()
    }

    return render(request, 'tags.html', data)


def custom_filters(request):
    data = {
        'cards': Card.objects.all()
    }

    return render(request, 'custom_filters.html', data)


def profile(request):
    return render(request, 'profile.html')


def faq(request):
    return render(request, 'faq.html')


def deal(request):
    data = {
        'cards': Card.objects.all()
    }
    return render(request, 'deal.html', data)

def blackjack(request):
    """
    ? is random number generator while :5 select the first two cards for the player.
    """
    data = {'cards': Card.objects.order_by('?')[:2]}

    return render(request, 'blackjack.html', data)


def poker(request):
    """
    ? is random number generator while :5 select the first five cards for the player.
    """
    data = {'cards': Card.objects.order_by('?')[:5]}

    return render(request, 'poker.html', data)

def hearts(request):
    '''
    Card.HEART is a better way for other people to refer to since we created this in our models.
    '''
    data = {'cards': Card.objects.filter(suit=Card.HEART)}

    return render(request, 'hearts.html', data)


def no_faces(request):
    '''
    Need to show, in a dictionary!!!! The use of 'in' is better than using exclude chaining.
    '''
    data = {'cards': Card.objects.exclude(rank__in=['jack', 'queen', 'king','ace'])}

    return render(request, 'no_faces.html', data)