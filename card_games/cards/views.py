from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render, redirect
from card_games import settings
from cards.forms import EmailUserCreationForm
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

@login_required
def profile(request):
    return render(request, 'profile.html', )


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
    if data['cards'][0].rank == 'ace' or data['cards'][1].rank == 'ace':
        user = request.user
        user.email_user("You got an Ace!", "Lets Ace It UP!", settings.DEFAULT_FROM_EMAIL)
    else:
        user = request.user
        user.email_user("#Failed Ace!", "You suck at this game!!", settings.DEFAULT_FROM_EMAIL)

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

def register(request):
    if request.method == 'POST':
        form = EmailUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            text_content = 'Thank you for signing up for our website, {} {}!'.format(user.first_name, user.last_name)
            html_content = '<h2>Thanks {} {} for signing up!</h2> <div>I hope you enjoy using our site</div>' \
                           '<p>You signed up at {}.</p>'.format(user.first_name, user.last_name, user.date_joined)
            msg = EmailMultiAlternatives("Welcome!", text_content, settings.DEFAULT_FROM_EMAIL, [user.email])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            return redirect("profile")
    else:
        form = EmailUserCreationForm()

    return render(request, "registration/register.html", {
        'form': form,
    })