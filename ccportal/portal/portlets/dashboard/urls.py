from django.conf.urls import patterns, url

import views

urlpatterns = patterns('',
    # ex: /thread/
    url(r'^$', views.index, name='index'),
    # ex: /thread/5/
    # url(r'^(?P<thead_id>\d+)/$', views.thead, name='thread'),
    # ex: /thread/5/vote/
    # url(r'^(?P< thead_id >\d+)/delete/$', delete, name='delete'),
)