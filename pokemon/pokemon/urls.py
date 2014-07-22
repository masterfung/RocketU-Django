from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'game.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^all_pokemon/$', 'game.views.all_pokemon', name='all_pokemon'),

	url(r'^new_pokemon/$', 'game.views.new_pokemon', name='new_pokemon'),

)
