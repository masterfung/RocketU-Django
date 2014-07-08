from django.forms import ModelForm
from brochure.models import Project, Contact

__author__ = '@masterfung'

class ProjectForm(ModelForm):
	class Meta:
		model = Project

class ContactForm(ModelForm):
	class Meta:
		model = Contact