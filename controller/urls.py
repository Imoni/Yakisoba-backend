from django.conf.urls.defaults import *

from controller import views
'''
Defines the url patterns for controller information
'''
urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^toggle/(?P<switch_id>\d+)/$', views.toggle_switch, name='toggle_switch'),
    url(r'^on/(?P<switch_id>\d+)/$', views.turn_on, name='turn_on'),
    url(r'^off/(?P<switch_id>\d+)/$', views.turn_off, name='turn_off'),
)
