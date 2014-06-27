from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=120)
    twitter = models.CharField(max_length=40, null=True)

    def __unicode__(self):
        return u"{}".format(self.name)