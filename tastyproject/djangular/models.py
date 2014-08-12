from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class UserUpload(models.Model):
	user = models.ForeignKey(User, related_name='user')
	media_name = models.CharField(max_length=50)
	media_file = models.FileField(upload_to='%Y/%m/%d')
	timestamp = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.media_name