from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'card_games.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	url(r'^$', 'cards.views.home', name='home'),
	url(r'^clubs/$', 'cards.views.clubs', name='clubs'),
	url(r'^diamonds_hearts/$', 'cards.views.diamonds_hearts', name='diamonds_hearts'),
	url(r'^spades/$', 'cards.views.spades', name='spades'),
	url(r'^faces/$', 'cards.views.faces', name='faces'),
	url(r'^cards_filters/$', 'cards.views.cards_filters', name='cards_filters'),
	url(r'^cards_filters/custom/$', 'cards.views.custom_filters', name='custom_filters'),
	url(r'^tags/$', 'cards.views.tags', name='tags'),

	url(r'^profile/$', 'cards.views.profile', name='profile'),

	url(r'^faq/$', 'cards.views.faq', name='faq'),
	url(r'^deal/$', 'cards.views.deal', name='deal'),
	url(r'^blackjack/$', 'cards.views.blackjack', name='blackjack'),
	url(r'^poker/$', 'cards.views.poker', name='poker'),
	url(r'^hearts/$', 'cards.views.hearts', name='hearts'),
	url(r'^no_faces/$', 'cards.views.no_faces', name='no_faces'),
	url(r'^war/$', 'cards.views.war', name='war'),

	url(r'^register/$', 'cards.views.register', name='register'),
	url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
	url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),

	url(r'^password_reset/$', 'django.contrib.auth.views.password_reset', name='password_reset'),
	url(r'^password_reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
	# Support old style base36 password reset links; remove in Django 1.7
	url(r'^reset/(?P<uidb36>[0-9A-Za-z]{1,13})-(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
		'django.contrib.auth.views.password_reset_confirm_uidb36'),
	url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
		'django.contrib.auth.views.password_reset_confirm',
		name='password_reset_confirm'),
	url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)