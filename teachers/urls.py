from django.conf.urls import patterns, url

from teachers import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<teacher_id>\d+)/$', views.detail, name='detail'),
    
)