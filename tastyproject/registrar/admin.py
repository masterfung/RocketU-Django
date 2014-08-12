from django.contrib import admin

# Register your models here.
from registrar.models import Klass, Student, StudentProject


admin.site.register(Klass)
admin.site.register(Student)
admin.site.register(StudentProject)
