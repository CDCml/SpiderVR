from django.conf.urls import patterns, include, url
from sub_vrworld import views


urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'bootstrap_demo.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^$', views.index, name='index'),
                       url(r'^news/$', views.new, name='new'),
                       url(r'^news_1/$', views.new_1, name='new_1'),
                       url(r'^videos/$', views.videos, name='videos'),
                       url(r'^forvr/$', views.forvr, name='forvr'),
                       url(r'^register/$', views.register, name='register'),
                       url(r'^login/$', views.user_login, name='user_login'),
                       url(r'^logout/$', views.user_logout, name = 'logout'),

                       )









