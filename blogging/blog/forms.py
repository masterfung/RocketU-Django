import re
from django import forms
from django.core.exceptions import ValidationError
from blog.models import Author, Comment, User, Post

def no_happiness(value):
	if re.match("happiness|joy|happy|smile]", value) is not None:
		raise ValidationError('You cant be happy here!')

class CommentForm(forms.Form):
	author = forms.ModelChoiceField(Author.objects.all())
	comment_body = forms.CharField(max_length=500, validators=[no_happiness])
	post = forms.ModelChoiceField(Post.objects.all())


class AuthorForm(forms.Form):
	name = forms.CharField(max_length=120)
	twitter = forms.CharField(max_length=40)
	age = forms.IntegerField()
	location = forms.CharField(max_length=30)

class PostForm(forms.Form):
	title = forms.CharField(max_length=120)
	body = forms.CharField(max_length=500)
	author = forms.ModelChoiceField(Author.objects.all())

class TagForm(forms.Form):
	name = forms.CharField(max_length=20)
	post = forms.ModelChoiceField(Post.objects.all())