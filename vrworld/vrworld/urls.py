from django.conf.urls import patterns, include, url
from django.contrib import admin
from sub_vrworld import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bootstrap_demo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$',views.index,name='index' ),
    url(r'^sub_vrworld/', include('sub_vrworld.urls')),
)
