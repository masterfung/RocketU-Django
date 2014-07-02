from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'favorites.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	url(r"^$", 'hollywood.views.home', name='home'),
	url(r'^genres/$', 'hollywood.views.genres', name='genres'),
	url(r'^movies/$', 'hollywood.views.movies', name='movies'),
	url(r'^actors/$', 'hollywood.views.actors', name='actors'),
	url(r'^genres/new/$', 'hollywood.views.new_genre', name='new_genre'),
	url(r'^movies/new/$', 'hollywood.views.new_movie', name='new_movie'),
	url(r'^actors/new/$', 'hollywood.views.new_actor', name='new_actor'),
	url(r'^genres/(?P<genre_id>\w+)/$', 'hollywood.views.view_genre', name='view_genre'),
	url(r'^movies/(?P<movie_id>\w+)/$', 'hollywood.views.view_movie', name='view_movie'),
	url(r'^actors/(?P<actor_id>\w+)/$', 'hollywood.views.view_actor', name='view_actor'),
	url(r'^genres/(?P<genre_id>\w+)/edit/$', 'hollywood.views.edit_genre', name='edit_genre'),
	url(r'^movies/(?P<movie_id>\w+)/edit/$', 'hollywood.views.edit_movie', name='edit_movie'),
	url(r'^actors/(?P<actor_id>\w+)/edit/$', 'hollywood.views.edit_actor', name='edit_actor'),
	url(r'^genres/(?P<genre_id>\w+)/delete/$', 'hollywood.views.delete_genre', name='delete_genre'),
	url(r'^actors/(?P<actor_id>\w+)/delete/$', 'hollywood.views.delete_actor', name='delete_actor'),
	url(r'^movies/(?P<movie_id>\w+)/delete/$', 'hollywood.views.delete_movie', name='delete_movie'),
)
