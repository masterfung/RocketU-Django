from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from django.contrib import admin
from snake import settings

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:

    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'game.views.home', name='home'),
    (r'^accounts/', include('registration.backends.default.urls')),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^game/$', 'game.views.game', name='game'),
    url(r'^leaderboard/$', 'game.views.leaderboard', name='leaderboard'),

)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)