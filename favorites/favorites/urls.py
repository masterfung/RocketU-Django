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
	url(r'^genres/new/$', 'hollywood.views.new_genre', name='new_genre'),
)
