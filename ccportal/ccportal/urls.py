from django.conf.urls import patterns, include, url

from django.contrib import admin

from ccportal.portlets import *


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'ccportal.portlets.dashboard.views.index', name='index'),

    # Admin
    url(r'^modeladmin/', include(admin.site.urls)),


)
