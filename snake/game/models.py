from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class ScoreKeeping(models.Model):
	user = models.ForeignKey(User)
	high_score = models.PositiveIntegerField(default=0)
	time = models.DateTimeField(auto_now_add=True)

	SNAKE = 'SK'
	MEMORY = 'MM'
	GAME_CHOICE = (

		(SNAKE, 'Snake'),
		(MEMORY, 'Memory'),

	)
	choice_of_game = models.CharField(max_length=2,
	                                  choices=GAME_CHOICE,
	                                  default=SNAKE)



	def __unicode__(self):
		return str(self.user)
