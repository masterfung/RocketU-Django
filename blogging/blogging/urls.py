from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blogging.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	url(r'^comment-form/$', 'blog.views.comment_logic', name='comment-form'),
	url(r'^author-form/$', 'blog.views.author_logic', name='author-form'),
	url(r'^comments/$', 'blog.views.comments', name='my_comment'),
	url(r'^authors/$', 'blog.views.authors', name='my_author'),
)
