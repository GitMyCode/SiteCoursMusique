from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^$', 'mysite.views.home', name='home'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^news/', include('news.urls', namespace='news')),
    url(r'^teachers/', include('teachers.urls', namespace='teachers')),
    url(r'^admin/', include(admin.site.urls))
)
