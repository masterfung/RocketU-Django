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
	power = models.CharField(max_length=60)

	def __unicode__(self):
		return u"{}".format(self.power)

class Boss(models.Model):
	name = models.CharField(max_length=100)
	age = models.IntegerField(max_length=3)
	gender = models.CharField(max_length=1)
	region = models.CharField(max_length=30)
	difficulty = models.ForeignKey(Level, related_name='difficulty')

	def __unicode__(self):
		return u"{}".format(self.name)

class Trainer(models.Model):
	name = models.CharField(max_length=100)
	age = models.IntegerField(max_length=3)
	gender = models.CharField(max_length=1)
	accessory = models.TextField()
	level = models.ForeignKey(Level, related_name='levels')

	def __unicode__(self):
		return u"{}".format(self.name)

class Pokemon(models.Model):
	name = models.CharField(max_length=100)
	health = models.IntegerField(max_length=2)
	type = models.ForeignKey(Type, related_name='types')
	power = models.ForeignKey(Power, related_name='powers')

	def __unicode__(self):
		return u"{}".format(self.name)