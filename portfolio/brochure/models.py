from django.db import models

# Create your models here.

class Language(models.Model):
	name = models.CharField(max_length=80)

	def __unicode__(self):
		return self.name

class Link(models.Model):
	name = models.CharField(max_length=80)
	link = models.CharField(max_length=120)

	def __unicode__(self):
		return self.name

class Project(models.Model):
	name = models.CharField(max_length=120)
	description = models.TextField()
	language = models.ForeignKey(Language, related_name='languages')
	image = models.ImageField(upload_to='images/')
	link = models.ForeignKey(Link, related_name='links')

	def __unicode__(self):
		return self.name

class Contact(models.Model):
	name = models.CharField(max_length=120)
	number = models.SmallIntegerField(null=True)
	email = models.EmailField()
	comment = models.TextField()

	def __unicode__(self):
		return "{} - {}".format(self.name, self.number)