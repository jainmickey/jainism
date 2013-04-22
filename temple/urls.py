from django.conf.urls import patterns, include,url

from temple.views import *

urlpatterns = patterns('',
    url(r'^$', temple_home, name='temple_home'),
    url(r'^(?P<pk>/d+)/$', TempleDetailView.as_view(), name='temple_detail'),
)
