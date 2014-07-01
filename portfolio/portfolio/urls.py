from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'portfolio.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/(?P<name>\w+)/(?P<color>\w+)$', 'brochure.views.hello'),
	url(r'^var/(?P<name>\w+)$', 'brochure.views.variable'),
	url(r"^scratchpad/(?P<first>\w+)/(?P<second>\w+)$", 'brochure.views.fizzbuzz'),
	url(r"^justice/$", 'brochure.views.justice'),
)
