from django.contrib import admin
from brochure.models import Language, Project, Link

# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
	list_display = ('name', 'description', 'language', 'link')

admin.site.register(Language)
admin.site.register(Link)
admin.site.register(Project, ProjectAdmin)
