from django.conf.urls import patterns, url

import views, endpoints

urlpatterns = patterns('',
    # ex: /thread/
    url(r'^$', views.users, name='index'),
    # ex: /thread/5/
    url(r'^users/$', views.users, name='users'),
    url(r'^groups/$', views.groups, name='users'),
    # ex: /thread/5/vote/
    # url(r'^(?P< thead_id >\d+)/delete/$', delete, name='delete'),

        # Root path: / 
    url(r'users/get/$', endpoints.user_list),


)