from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'ccportal.portlets.dashboard.views.index', name='index'),
    url(r'^modeladmin/', include(admin.site.urls)),

)
