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
	url(r'^movie/new/$', 'hollywood.views.new_movie', name='new_movie'),
	url(r'^genres/(?P<genre_id>\w+)/$', 'hollywood.views.view_genre', name='view_genre'),
	url(r'^movies/(?P<movie_id>\w+)/$', 'hollywood.views.view_movie', name='view_movie'),
	url(r'^actors/(?P<actor_id>\w+)/$', 'hollywood.views.view_actor', name='view_actor'),
)
