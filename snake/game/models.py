from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class ScoreKeeping(models.Model):
	user = models.ForeignKey(User)
	high_score = models.PositiveIntegerField(default=0)

	def __unicode__(self):
		return self.username
