from django.contrib import admin
from blog.models import Author, Post, User, Comment, Tag

# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
	list_display = ('name', 'twitter', 'age', 'location')

class UserAdmin(admin.ModelAdmin):
	list_display = ('name', 'age', 'location', 'email', 'username')

admin.site.register(Author, AuthorAdmin)
admin.site.register(Post)
admin.site.register(User, UserAdmin)
admin.site.register(Comment)
admin.site.register(Tag)