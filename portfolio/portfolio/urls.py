from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'portfolio.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'brochure.views.hello', name='home'),
	url(r'^contact/$', 'brochure.views.contact'),
	# url(r"^scratchpad/(?P<first>\w+)/(?P<second>\w+)$", 'brochure.views.fizzbuzz'),
	url(r"^portfolio/$", 'brochure.views.portfolio', name='portfolio'),
)
