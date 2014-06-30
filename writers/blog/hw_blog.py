#1
def return_blog_post_comment(post_id):
	post = Post.objects.get(pk=post_id)
	return post.post_comments.all()

print return_blog_post_comment(1)


#2
def returns_votes(post_id):
	votes = Post.objects.get(pk=post_id)
	return votes.user_votes.count()

print returns_votes(1)


#3
def all_comments(user_id):
	comments = User.objects.get(pk=user_id)
	return comments.user_comments.all()

print all_comments(2)


#4
def all_pk_1():
	return Tag.objects.filter(posts__uservotes__pk=2)

print all_pk_1()


#5





# first = Post.objects.get(pk=1)
# >>> print first
# First!
# >>> second = User.objects.get(pk=2)
# >>> print second
# Ben Kremer
# >>> first.posts.add(second)
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# AttributeError: 'Post' object has no attribute 'posts'
# >>> first.user_votes.add(second)