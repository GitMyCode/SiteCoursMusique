from django.conf.urls import patterns, include, url
from django.views.generic.base import RedirectView

from django.contrib import admin
from django.conf import settings
admin.autodiscover()

from core import views



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sitemusique.views.home', name='home'),
    # url(r'^sitemusique/', include('sitemusique.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^$', RedirectView.as_view(url='/admin')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^acceuil/$', views.acceuil, name='acceuil'),
    url(r'^gallerie/', include('photologue.urls')),


    # Permet de d'acceder a l'url des photo dans le repertoire media
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}),
)
