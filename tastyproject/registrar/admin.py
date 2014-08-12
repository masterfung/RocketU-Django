from django.contrib import admin

# Register your models here.
from registrar.models import Klass, Student


admin.site.register(Klass)
admin.site.register(Student)
