from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'explore.views.home', name='home'),
    url(r'^explore/(?P<entity_id>\d+)/$', 'explore.views.explore'),
)
