from django.conf.urls import patterns, include, url
from django.contrib import admin
from myapp import views

urlpatterns = patterns('',
    url('^$', views.home, name='home'),
    url('^login/$', 'django.contrib.auth.views.login', name='login'),
    url('^logout/$', 'django.contrib.auth.views.logout_then_login', name='logout'),
    url('^user/(?P<username>\w+)/$', views.user_detail, name='user_detail'),
    url('^project/$', views.ProjectList.as_view(), name='project_list'),
    url('^project/(?P<pk>\d+)/$', views.ProjectDetail.as_view(), name='project_detail'),
)