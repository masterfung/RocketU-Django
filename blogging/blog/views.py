from django.shortcuts import render, render_to_response, redirect
from blog.models import Comment, Author
from blog.forms import CommentForm, AuthorForm


def comments(request):
	comments = Comment.objects.all()
	return render_to_response("view_comments.html", {'comments': comments})

def authors(request):
	authors = Author.objects.all()
	return render_to_response("view_authors.html", {'authors': authors})

#forms

def comment_form(request):
	data = {"comment_form": CommentForm()}
	return render(request, "comment_form.html", data)


def author_form(request):
	data = {"author_form": AuthorForm()}
	return render(request, "author_form.html", data)

#form logic
def comment_logic(request):
	if request.method == "POST":
		form = CommentForm(request.POST)
		if form.is_valid():
			# Get the instance of the form filled with the submitted data
			author = form.cleaned_data['author']
			comment_body = form.cleaned_data['comment_body']
			post = form.cleaned_data['post']
			Comment.objects.create(posts=post, text=comment_body, user=author)

			return redirect("/comments")

	# Else if the user is looking at the form page
	else:
		form = CommentForm()
	comments = Comment.objects.all()
	data = {'comment_form': form}
	return render(request, "comment_form.html", data)


def author_logic(request):
	if request.method == "POST":
		form = AuthorForm(request.POST)
		if form.is_valid():
			# Get the instance of the form filled with the submitted data
			name = form.cleaned_data['name']
			twitter = form.cleaned_data['twitter']
			age = form.cleaned_data['age']
			location = form.cleaned_data['location']
			Author.objects.create(name=name, twitter=twitter, age=age, location=location)

		return redirect("/authors")

	# Else if the user is looking at the form page
	else:
		form = AuthorForm()
		authors = Author.objects.all()
		data = {'author_form': form}
	return render(request, "author_form.html", data)