from django.contrib import admin
from blog.models import Author, Comment, Tag, Post, User

# Register your models here.

admin.site.register(Author)
admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(User)