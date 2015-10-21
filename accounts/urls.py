from django.conf.urls import *
from accounts import views
from django.contrib.auth.views import login, logout

urlpatterns = patterns('',
    url(r'^login/$', login, {'template_name':'accounts/login.html'},name='login'),
    url(r'^logout/$', logout, {'next_page':'/'},name='logout'),
    url(r'^register/$', 'accounts.views.registration',name='register'),
    url(r'^profile/$', views.Profile.as_view(),name='profile'),
)