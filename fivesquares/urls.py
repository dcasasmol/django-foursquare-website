from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$', 'foursquareapi.views.home', name='home'),
    url(r'^query/$', 'foursquareapi.views.query', name='query'),
#    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('social_auth.urls')),
)
