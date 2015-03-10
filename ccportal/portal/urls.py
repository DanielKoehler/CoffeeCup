from django.conf.urls import patterns, include, url

from django.contrib import admin

# from portal.portlets import messenger


admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', 'portal.portlets.dashboard.views.index', name='index'),

    url(r'^dashboard/', include('portal.portlets.dashboard.urls')),
    url(r'^messenger/', include('portal.portlets.messenger.urls')),

    # Admin
    url(r'^modeladmin/', include(admin.site.urls)),
    
)
