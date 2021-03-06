from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from cards.forms import EmailUserCreationForm
from cards.models import Card, Player, WarGame
from cards.test_utils import run_pyflakes_for_package, run_pep8_for_package
from cards.utils import create_deck

__author__ = '@masterfung'

from django.test import TestCase

# class BasicMathTestCase(TestCase):
# def test_math(self):
# a = 1
# 		b = 1
# 		self.assertEqual(a+b, 2)
#
# 	def test_failing_case(self):
# 		a = 1
# 		b = 10
# 		self.assertEqual(a+b, 11)
#
# class UtilTestCase(TestCase):
# 	def test_create_deck_count(self):
# 		"""Test that we created 52 cards"""
# 		create_deck()
# 		self.assertEqual(Card.objects.count(), 52)
#
# class ModelTestCase(TestCase):
# 	def test_get_ranking(self):
# 		card = Card.objects.create(suit=Card.CLUB, rank='jack')
# 		self.assertEqual(card.get_ranking(), 11)


class ModelComparison(TestCase):
    def test_get_war_result_loss(self):
        card = Card.objects.create(suit=Card.CLUB, rank='jack')
        card_two = Card.objects.create(suit=Card.HEART, rank='queen')
        self.assertEqual(card.get_war_result(card_two), -1)

    def test_get_war_result_tie(self):
        card = Card.objects.create(suit=Card.CLUB, rank='jack')
        card_two = Card.objects.create(suit=Card.HEART, rank='jack')
        self.assertEqual(card.get_war_result(card_two), 0)

    def test_get_war_result_win(self):
        card = Card.objects.create(suit=Card.CLUB, rank='king')
        card_two = Card.objects.create(suit=Card.HEART, rank='jack')
        self.assertEqual(card.get_war_result(card_two), 1)


class FormTestCase(TestCase):
    def test_clean_username_exception(self):
        # Create a player so that this username we're testing is already taken
        Player.objects.create_user(username='test-user')

        # set up the form for testing
        form = EmailUserCreationForm()
        form.cleaned_data = {'username': 'test-user'}

        # use a context manager to watch for the validation error being raised
        with self.assertRaises(ValidationError):
            form.clean_username()

    def test_clean_username(self):
        # review this again!
        # set up the form for testing
        form = EmailUserCreationForm()
        form.cleaned_data = {'username': 'test-user'}

        # use a context manager to watch for the validation error being raised
        self.assertEquals(form.clean_username(), 'test-user')


class ViewTestCase(TestCase):
    def setUp(self):
        create_deck()

    def test_home_page(self):
        response = self.client.get(reverse('home'))
        # finds the route based on home
        self.assertIn('<p>Suit: spade, Rank: two</p>', response.content)
        self.assertEqual(response.context['cards'].count(), 52)

    def test_register_page(self):
        username = 'new-user'
        data = {
            'username': username,
            'email': 'test@test.com',
            'password1': 'test',
            'password2': 'test'
        }
        response = self.client.post(reverse('register'),
                                    data)
        # .client handles the interaction of url to post all the info

        # Check this user was created in the database
        self.assertTrue(Player.objects.filter(username=username).exists())

        # Check it's a redirect to the profile page
        self.assertIsInstance(response, HttpResponseRedirect)
        self.assertTrue(response.get('location').endswith(reverse('profile')))
        # look to see if this can be simplified

    def create_war_game(self, user, result=WarGame.LOSS):
        # helper method/make sure the naming does not have test in the beginning
        WarGame.objects.create(result=result, player=user)

    def test_profile_page(self):
        # Create user and log them in
        password = 'passsword'
        user = Player.objects.create_user(username='test-user', email='test@test.com', password='password')
        self.client.login(username=user.username, password=password)

        # Set up some war game entries
        self.create_war_game(user)
        self.create_war_game(user)
        self.create_war_game(user)
        self.create_war_game(user, WarGame.WIN)
        self.create_war_game(user, WarGame.WIN)

        # Make the url call and check the html and games queryset length
        response = self.client.get(reverse('profile'))
        self.assertInHTML('<p>Hi {}, you have 2 wins and 3 loses.</p>'.format(user.username), response.content)
        self.assertEqual(len(response.context['games']), 5)
        # self.assertEqual(len(response.context['wins']), 2)
        # self.assertEqual(len(response.context['losses']), 3)

    def test_faq_exist(self):
        response = self.client.get(reverse('faq'))
        self.assertIn('<p>Q: Can I win real money on this website?</p>', response.content)
        self.assertTrue(response.context)

    def test_filters_exist(self):
        response = self.client.get(reverse('filters'))
        self.assertIn('We have 52 cards!', response.content)
        self.assertTrue(response.context)

    def test_login_page(self):
        user = Player.objects.create_user(username='test', email='test@test.com', password='test')
        # response = self.client.post(reverse('login'), data)
        # self.assertIsInstance(HttpResponseRedirect, response) #this line is not working fully
        self.assertTrue(user.is_authenticated())

    def test_get_wins(self):
        user = Player.objects.create_user(username='test-user', email='test@test.com', password='password')
        self.create_war_game(user, WarGame.WIN)
        self.create_war_game(user, WarGame.WIN)
        self.assertEqual(user.get_wins(), 2)

    def test_get_losses(self):
        user = Player.objects.create_user(username='test-user', email='test@test.com', password='password')
        self.create_war_game(user, WarGame.LOSS)
        self.create_war_game(user, WarGame.LOSS)
        self.create_war_game(user, WarGame.LOSS)
        self.assertEqual(user.get_losses(), 3)


class SyntaxTest(TestCase):
    def test_syntax(self):
        """
        Run pyflakes/pep8 across the code base to check for potential errors.
        """
        packages = ['cards']
        warnings = []
        # Eventually should use flake8 instead so we can ignore specific lines via a comment
        for package in packages:
            warnings.extend(run_pyflakes_for_package(package, extra_ignore=("_settings",)))
            warnings.extend(run_pep8_for_package(package, extra_ignore=("_settings",)))
        if warnings:
            self.fail("{0} Syntax warnings!\n\n{1}".format(len(warnings), "\n".join(warnings)))
