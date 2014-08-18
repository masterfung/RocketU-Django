from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from django.contrib import admin
from tastypie.api import Api
from djangular.api.resources import MediaResource
from registrar.api.resources import StudentResource, ClassResource, StudentProjectResource

admin.autodiscover()

v1_api = Api(api_name="v1")
v1_api.register(StudentResource())
v1_api.register(ClassResource())
v1_api.register(StudentProjectResource())
v1_api.register(MediaResource())

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tastyproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(v1_api.urls)),
    url(r'api/doc/', include('tastypie_swagger.urls', namespace='tastypie_swagger'),
    kwargs={"tastypie_api_module": "v1_api",
            "namespace": "tastypie_swagger"}
    ),
    url(r'^$', 'djangular.views.home', name='home'),
    url(r'^a/$', 'djangular.views.angular', name='angular'),
	url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)