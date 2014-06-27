from django.db import models

# Create your models here.

class Author(models.Model):
	name = models.CharField(max_length=120)
	twitter = models.CharField(max_length=40, null=True)

	def __unicode__(self):
		return u"{}".format(self.name)


class Post(models.Model):
	title = models.CharField(max_length=120)
	body = models.TextField()
	author = models.ForeignKey(Author, related_name='posts')

	def __unicode__(self):
		return u"{}".format(self.title)


class Tag(models.Model):
	name = models.CharField(max_length=20)
	posts = models.ManyToManyField(Post)

	def __unicode__(self):
		return u"{}".format(self.name)


class User(models.Model):
	pass

class Comment(models.Model):
	pass

class Comment(models.Model):
	pass