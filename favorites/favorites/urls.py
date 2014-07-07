from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'favorites.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	url(r"^$", 'hollywood.views.home', name='home'),
	(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.STATIC_ROOT
        }),
	(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT, 'show_indexes': False
        }),
	url(r'^genres/$', 'hollywood.views.genres', name='genres'),
	url(r'^movies/$', 'hollywood.views.movies', name='movies'),
	url(r'^actors/$', 'hollywood.views.actors', name='actors'),
	url(r'^videos/$', 'hollywood.views.videos', name='videos'),
	url(r'^genres/new/$', 'hollywood.views.new_genre', name='new_genre'),
	url(r'^movies/new/$', 'hollywood.views.new_movie', name='new_movie'),
	url(r'^actors/new/$', 'hollywood.views.new_actor', name='new_actor'),
	url(r'^videos/new/$', 'hollywood.views.new_video', name='new_video'),
	url(r'^genres/(?P<genre_id>\w+)/$', 'hollywood.views.view_genre', name='view_genre'),
	url(r'^movies/(?P<movie_id>\w+)/$', 'hollywood.views.view_movie', name='view_movie'),
	url(r'^actors/(?P<actor_id>\w+)/$', 'hollywood.views.view_actor', name='view_actor'),
	url(r'^videos/(?P<video_id>\w+)/$', 'hollywood.views.view_video', name='view_video'),
	url(r'^genres/(?P<genre_id>\w+)/edit/$', 'hollywood.views.edit_genre', name='edit_genre'),
	url(r'^movies/(?P<movie_id>\w+)/edit/$', 'hollywood.views.edit_movie', name='edit_movie'),
	url(r'^actors/(?P<actor_id>\w+)/edit/$', 'hollywood.views.edit_actor', name='edit_actor'),
	url(r'^videos/(?P<video_id>\w+)/edit/$', 'hollywood.views.edit_video', name='edit_video'),
	url(r'^genres/(?P<genre_id>\w+)/delete/$', 'hollywood.views.delete_genre', name='delete_genre'),
	url(r'^actors/(?P<actor_id>\w+)/delete/$', 'hollywood.views.delete_actor', name='delete_actor'),
	url(r'^movies/(?P<movie_id>\w+)/delete/$', 'hollywood.views.delete_movie', name='delete_movie'),
	url(r'^videos/(?P<video_id>\w+)/delete/$', 'hollywood.views.delete_video', name='delete_video'),
)
