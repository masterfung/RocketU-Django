from django.db import models

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class Movie(models.Model):
    name = models.CharField(max_length=100)
    release_year = models.PositiveSmallIntegerField()
    genre = models.ForeignKey(Genre)

    def __unicode__(self):
        return self.name


class Actor(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveSmallIntegerField()
    movies = models.ManyToManyField(Movie)

    def __unicode__(self):
        return self.name