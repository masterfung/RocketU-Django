from django.shortcuts import render, render_to_response, redirect
from blog.models import Comment, Author, Post, Tag
from blog.forms import CommentForm, AuthorForm, PostForm, TagForm


def home(request):
	return render(request, "home.html")

def comments(request):
	comments = Comment.objects.all()
	return render_to_response("view_comments.html", {'comments': comments})

def authors(request):
	authors = Author.objects.all()
	return render_to_response("view_authors.html", {'authors': authors})

def posts(request):
	posts = Post.objects.all()
	return render_to_response("view_posts.html", {'posts': posts})

def tags(request):
	tags = Tag.objects.all()
	return render_to_response("view_tags.html", {'tags': tags})

#forms

def comment_form(request):
	data = {"comment_form": CommentForm()}
	return render(request, "comment_form.html", data)


def author_form(request):
	data = {"author_form": AuthorForm()}
	return render(request, "author_form.html", data)

def post_form(request):
	data = {"post_form": PostForm()}
	return render(request, "post_form.html", data)


def tag_form(request):
	data = {"tag_form": TagForm()}
	return render(request, "tag_form.html", data)

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

def post_logic(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			# Get the instance of the form filled with the submitted data
			title = form.cleaned_data['title']
			body = form.cleaned_data['body']
			author = form.cleaned_data['author']
			Post.objects.create(title=title, body=body, author=author)

			return redirect("/posts")

	# Else if the user is looking at the form page
	else:
		form = PostForm()
	posts = Post.objects.all()
	data = {'post_form': form}
	return render(request, "post_form.html", data)

def tag_logic(request):
	if request.method == "POST":
		form = TagForm(request.POST)
		if form.is_valid():
			# Get the instance of the form filled with the submitted data
			name = form.cleaned_data['name']
			Tag.objects.create(name=name)

			return redirect("/tags")

	# Else if the user is looking at the form page
	else:
		form = TagForm()
	tags = Tag.objects.all()
	data = {'tag_form': form}
	return render(request, "tag_form.html", data)