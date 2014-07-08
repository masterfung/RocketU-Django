from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'portfolio.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'brochure.views.hello', name='home'),
	url(r'^contact/$', 'brochure.views.contact', name='contact'),
	# url(r"^scratchpad/(?P<first>\w+)/(?P<second>\w+)$", 'brochure.views.fizzbuzz'),
	url(r"^portfolio/$", 'brochure.views.portfolio', name='portfolio'),
	url(r"^about/$", 'brochure.views.about', name='about'),
	url(r"^entrepreneur/$", 'brochure.views.entrepreneur', name='entrepreneur'),
	url(r"^hacker/$", 'brochure.views.hacker', name='hacker'),
	url(r"^artist/$", 'brochure.views.artist', name='artist'),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)