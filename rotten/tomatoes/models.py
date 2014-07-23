from django.db import models

# Create your models here.

class Movie(models.Model):
	title = models.CharField(max_length=100)
	release_year = models.PositiveSmallIntegerField()
	critics_score = models.IntegerField(null=True)
	poster = models.URLField()
	mpaa_rating = models.CharField(max_length=20, null=True)
	runtime = models.PositiveSmallIntegerField(null=True)
	audience_score = models.IntegerField(max_length=10, null=True, blank=True)

	def __unicode__(self):
		return self.title
