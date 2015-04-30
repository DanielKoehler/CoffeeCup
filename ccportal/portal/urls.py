from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin

admin.site.site_header = 'coffeeadmin'

# from portal.portlets import messenger

admin.autodiscover()

urlpatterns = patterns('',

	# Login 

    url(r'^login/$', 'portal.site.views.user_login'),
	url(r'^logout/$', 'portal.site.views.user_logout'),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url('', include('django.contrib.auth.urls', namespace='auth')),

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
    url(r'^admin/', include(admin.site.urls)),
    
)

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))
