from django.conf.urls import patterns, url

import views, endpoints

urlpatterns = patterns('',
    # ex: /thread/
    url(r'^$', views.index, name='index'),
    # ex: /thread/5/
    # url(r'^(?P<thead_id>\d+)/$', views.thead, name='thread'),

    # Root path: / 
    url(r'directory/get/$', endpoints.get_base),
    url(r'directory/get/(?P<objectId>.+)$', endpoints.get_directory),

    url(r'directory/post/$', endpoints.post_directory),

    url(r'directory/post/(?P<objectId>.+)$', endpoints.post_directory_rename),


    url(r'objects/delete/$', endpoints.delete_object),
    url(r'objects/post/$', endpoints.post_object),
    url(r'object/serve/(?P<objectId>.+)$', endpoints.serve_object),

    # File info
    url(r'file/get/(?P<objectId>.+)$', endpoints.get_object), 

    


)