
from django.conf.urls import patterns, url

from tracker import views

urlpatterns = patterns('',
            url(r'^$', views.home, name='index')
            )
