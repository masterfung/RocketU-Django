from django.conf.urls import patterns, include, url

from django.contrib import admin
from tastypie.api import Api
from registrar.api.resources import StudentResource, ClassResource

admin.autodiscover()

v1_api = Api(api_name="v1")
v1_api.register(StudentResource())
v1_api.register(ClassResource())

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tastyproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(v1_api.urls)),
)
