from django.conf.urls import patterns, include, url
from django.contrib import admin
from scoreboard import views
from django.conf import settings

from scoreboard.models import Scoreboard
from django.views.generic import ListView, DetailView

from django.conf.urls import *
from django.contrib.auth.views import login, logout

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^$', views.home, name = 'home'),
    url(r'^list/', views.ScoreboardList.as_view(context_object_name="scoreboard_list"), name = "scoreboard_list"),
    url(r'^scoreboard/(?P<pk>\d+)$', views.ScoreboardDetail.as_view(), name = 'scoreboard_detail'),
    url(r'^scoreboard/(?P<pk>\d+)/edit/$', views.ScoreboardUpdate.as_view(), name = 'scoreboard_update'),
    url(r'^spectator/', views.spectator, name = 'spectator'),
    
    url(r'^accounts/', include('accounts.urls')),
    
    
    url(r'^notfound/', views.notfound, name = 'notfound'),
    url(r'^people/(?P<score_id>[\w{}.-]{1,40})/$', views.people, name = 'people'),


    
)

urlpatterns += patterns(
    'django.views.static',
    (r'^media/images/(?P<path>.*)',
    'serve',
    {'document_root': settings.MEDIA_ROOT}),
)
