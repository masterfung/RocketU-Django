from django.db import models

# Create your models here.


class Level(models.Model):
	level = models.CharField(max_length=50)

	def __unicode__(self):
		return u"{}".format(self.level)

class Type(models.Model):
	type = models.CharField(max_length=60)

	def __unicode__(self):
		return u"{}".format(self.type)

class Power(models.Model):
	pass

	def __unicode__(self):
		return u"{}".format(self.name)

class Trainer(models.Model):
	name = models.CharField(max_length=100)
	age = models.IntegerField(max_length=3)
	gender = models.CharField(max_length=1)
	level = models.ForeignKey(Level, related_name='levels')

	def __unicode__(self):
		return u"{}".format(self.name)

class Pokemon(models.Model):
	name = models.CharField(max_length=100)
	type = models.ForeignKey(Type, related_name='pokemon_types')

	def __unicode__(self):
		return u"{}".format(self.name)