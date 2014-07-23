from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'rotten.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'tomatoes.views.home', name='home'),
	url(r'^new_movie_json/$', 'tomatoes.views.new_movie_json', name='new_movie_json'),
    url(r'^new_movie_html/$', 'tomatoes.views.new_movie_html', name='new_movie_html'),
    url(r'^favorites/$', 'tomatoes.views.all_favorites', name='all_favorites'),
    url(r'^tinder/$', 'tomatoes.views.tinder', name='tinder'),
    url(r'^new_favorite/$', 'tomatoes.views.new_favorite', name='new_favorite'),
)
