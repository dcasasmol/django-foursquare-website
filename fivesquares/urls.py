from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # url(r'^$', 'fivesquares.views.home', name='home'),
    # url(r'^fivesquares/', include('fivesquares.foo.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
