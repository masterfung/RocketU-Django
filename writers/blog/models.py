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
	votes = models.ManyToManyField(User, related_name='username')

	def __unicode__(self):
		return u"{}".format(self.title)


class Tag(models.Model):
	name = models.CharField(max_length=20)
	posts = models.ManyToManyField(Post, related_name='tags')

	def __unicode__(self):
		return u"{}".format(self.name)

class User(models.Model):
	name = models.CharField(max_length=20)
	email = models.EmailField(max_length=70)
	username = models.CharField(max_length=20)

	def __unicode__(self):
		return u"{}".format(self.name)

class Comment(models.Model):
	text = models.TextField()
	posts = models.ForeignKey(User)

	def __unicode__(self):
		return u"{}".format(self.text)
