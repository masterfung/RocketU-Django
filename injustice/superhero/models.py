from django.db import models

# Create your models here.

class Player(models.Model):
	superhero_name = models.CharField(max_length=120)
	real_name = models.CharField(max_length=120)
	type = models.CharField(max_length=5)
	age = models.IntegerField(max_length=3)

	def __unicode__(self):
		return u"{}".format(self.real_name)

class Team(models.Model):
	name = models.CharField(max_length=50)
	alliance = models.ForeignKey(Player, related_name='affiliations')

	def __unicode__(self):
		return u"{}".format(self.name)

class Power(models.Model):
	power = models.TextField()
	good_bad = models.ForeignKey(Player, related_name='powers')

	def __unicode__(self):
		return u"{}".format(self.power)

class Location(models.Model):
	fighting_location = models.CharField(max_length=50)
	tournament = models.ManyToManyField(Team, related_name='teams')

	def __unicode__(self):
		return u"{}".format(self.fighting_location)