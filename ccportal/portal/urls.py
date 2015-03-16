from django.conf.urls import patterns, include, url

from django.contrib import admin

# from portal.portlets import messenger


admin.autodiscover()

urlpatterns = patterns('',

	# Login 

	url(r'^login/$', 'portal.site.views.login'),

	# Portlets
    url(r'^$', 'portal.portlets.dashboard.views.index', name='index'),
    url(r'^dashboard/', include('portal.portlets.dashboard.urls')),
    url(r'^messenger/', include('portal.portlets.messenger.urls')),
    url(r'^equipmentmanager/', include('portal.portlets.equipmentmanager.urls')),
    url(r'^locationmanager/', include('portal.portlets.locationmanager.urls')),
    url(r'^useradministration/', include('portal.portlets.useradministration.urls')),
    url(r'^mediasharing/', include('portal.portlets.mediasharing.urls')),
    url(r'^scheduling/', include('portal.portlets.scheduling.urls')),
    url(r'^investorbulletin/', include('portal.portlets.investorbulletin.urls')),

    # Admin
    url(r'^modeladmin/', include(admin.site.urls)),
    
)
