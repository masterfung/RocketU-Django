from cards.models import Card
from cards.utils import create_deck

__author__ = '@masterfung'

from django.test import TestCase

# class BasicMathTestCase(TestCase):
# 	def test_math(self):
# 		a = 1
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