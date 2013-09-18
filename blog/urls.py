from django.conf.urls import patterns, url

urlpatterns = patterns('blog.views',
    url(r'^blog/$', 'home'),
    url(r'^$', 'tpl'),
    url(r'^addition/(?P<nombre1>\d+)/(?P<nombre2>\d+)/$', 'addition'),
)
