from django.db import models
from embed_video.fields import EmbedVideoField

# Create your models here.

class Genre(models.Model):
	name = models.CharField(max_length=100)

	def __unicode__(self):
		return self.name

class Video(models.Model):
	name = models.CharField(max_length=150)
	video = EmbedVideoField()

	def __unicode__(self):
		return self.video

class Movie(models.Model):
	name = models.CharField(max_length=100)
	release_year = models.PositiveSmallIntegerField()
	length = models.PositiveSmallIntegerField()
	picture = models.ImageField(upload_to='movies/')
	imdb = models.CharField(max_length=200)
	genre = models.ForeignKey(Genre, related_name='genres')
	video = models.ForeignKey(Video, related_name='videos')

	def __unicode__(self):
		return self.name

class Actor(models.Model):
	name = models.CharField(max_length=100)
	age = models.PositiveSmallIntegerField()
	movies = models.ManyToManyField(Movie)

	def __unicode__(self):
		return self.name

