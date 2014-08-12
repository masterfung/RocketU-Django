from tastypie.authorization import Authorization
from tastypie.fields import ToManyField

__author__ = 'htm'

from tastypie.resources import ModelResource
from registrar.models import Student, Klass


class BareClassResource(ModelResource):
	class Meta:
		queryset = Klass.objects.all()
		resource_name = "bare_class"


class StudentResource(ModelResource):
	klass = ToManyField('registrar.api.resources.ClassResource', 'klass', full=False)

	class Meta:
		queryset = Student.objects.all()
		resource_name = "student"
		allowed_methods = ['get', 'post', 'put', 'delete']  # Limit the possible REST actions
		fields = ['first_name', 'id']                       # Return only these fields in the response's data
		excludes = ['end_date']                             # Return all the fields except the ones specified
		always_return_data = True                           # Whether data should be returned when a POST is made
		limit = 20                                          # Number of objects per call in the list for pagination
		ordering = ['first_name', 'last_name']              # Default the order of the objects returned in this list
		authorization = Authorization()


class ClassResource(ModelResource):
	students = ToManyField(StudentResource, 'students', full=True)
	# false makes the students appear as link rather than list them out

	class Meta:
		queryset = Klass.objects.all()
		resource_name = "class"
		allowed_methods = ['get', 'post', 'put']  # Limit the possible REST actions
		fields = ['title']                 # Return only these fields in the response's data
		excludes = ['end_date']            # Return all the fields except the ones specified
		always_return_data = True          # Whether data should be returned when a POST is made
		limit = 20                         # Number of objects per call in the list for pagination
		ordering = ['title']         # Default the order of the objects returned in this list
		authorization = Authorization()