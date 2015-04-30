from django.conf.urls import patterns, url

import views, endpoints

urlpatterns = patterns('',
    # ex: /thread/
    url(r'^$', views.index, name='index'),
    # ex: /thread/5/
    url(r'events/get/$', endpoints.get_events),
    # ex: /thread/5/vote/
    # url(r'^(?P< thead_id >\d+)/delete/$', delete, name='delete'),
)