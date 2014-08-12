from django.contrib.auth.models import User
from tastypie.authorization import Authorization
from tastypie.cache import SimpleCache
from tastypie.constants import ALL_WITH_RELATIONS
from tastypie.fields import ToManyField, ToOneField
from djangular.models import UserUpload

__author__ = 'htm'

from tastypie.resources import ModelResource


class UserResource(ModelResource):
	class Meta:
		queryset = User.objects.all()


class MediaResource(ModelResource):
	user = ToOneField(UserResource, 'user', full=True)

	class Meta:
		queryset = UserUpload.objects.all()
		resource_name = 'media'
		allowed_methods = ['get', 'post', 'put', 'delete']
		authorization = Authorization()


# class BareClassResource(ModelResource):
# 	class Meta:
# 		queryset = Klass.objects.all()
# 		resource_name = "bare_class"
#
#
# class StudentProjectResource(ModelResource):
# 	student = ToOneField('registrar.api.resources.StudentResource', 'project', full=True, null=True)
#
# 	class Meta:
# 		queryset = StudentProject.objects.all()
# 		resource_name = 'project'
# 		allowed_methods = ['get', 'post', 'put', 'delete']
# 		authorization = Authorization()
#
#
# class StudentResource(ModelResource):
# 	klass = ToOneField('registrar.api.resources.ClassResource', 'klass', full=False)
# 	projects = ToManyField('registrar.api.resources.StudentProjectResource', 'projects', full=False)
#
# 	class Meta:
# 		queryset = Student.objects.all()
# 		resource_name = "student"
# 		allowed_methods = ['get', 'post', 'put', 'delete']  # Limit the possible REST actions
# 		# fields = ['first_name', 'id']                       # Return only these fields in the response's data
# 		# excludes = ['end_date']                             # Return all the fields except the ones specified
# 		always_return_data = True                             # Whether data should be returned when a POST is made
# 		limit = 20  # Number of objects per call in the list for pagination
# 		ordering = ['first_name', 'last_name']  # Default the order of the objects returned in this list
# 		authorization = Authorization()
# 		cache = SimpleCache(timeout=60000)
#
#
# class ClassResource(ModelResource):
# 	students = ToManyField(StudentResource, 'students', full=True, null=True)
#
# 	# false makes the students appear as link rather than list them out
#
# 	class Meta:
# 		queryset = Klass.objects.all()
# 		resource_name = "class"
# 		allowed_methods = ['get', 'post', 'put']  # Limit the possible REST actions
# 		# fields = ['title']                 # Return only these fields in the response's data
# 		# excludes = ['end_date']            # Return all the fields except the ones specified
# 		always_return_data = True  # Whether data should be returned when a POST is made
# 		# limit = 20                         # Number of objects per call in the list for pagination
# 		# ordering = ['title']         # Default the order of the objects returned in this list
# 		filtering = {
# 			'students': ALL_WITH_RELATIONS,
# 			'title': ['contains', 'icontains'],  # match exact and inexact titles
# 			'start_date': ['gt', ]
# 		}
# 		authorization = Authorization()


