from django.db import models

# Create your models here.

class Location(models.Model):
	fighting_location = models.CharField(max_length=50)

	def __unicode__(self):
		return u"{}".format(self.fighting_location)

class Alliance(models.Model):
	affiliation = models.CharField(max_length=20)

	def __unicode__(self):
		return u"{}".format(self.affiliation)

class Player(models.Model):
	superhero_name = models.CharField(max_length=120)
	real_name = models.CharField(max_length=120)
	type = models.CharField(max_length=5)
	age = models.IntegerField(max_length=3)
	location = models.ForeignKey(Location, related_name='locations')
	affiliation = models.ForeignKey(Alliance, related_name='alliance')

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

