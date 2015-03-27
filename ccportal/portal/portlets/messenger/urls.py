from django.conf.urls import patterns, url

import views

urlpatterns = patterns('',
    # ex: /thread/
    url(r'^$', views.index, name='index'),
    
)
