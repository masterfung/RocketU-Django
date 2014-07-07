from django.conf.urls import patterns, include, url

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
)

