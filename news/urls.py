from django.conf.urls import patterns, url

from news import views

urlpatterns = patterns('',
    # ex: /polls/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # ex: /polls/5/
    url(r'^(?P<pk>\d+)/$',views.DetailView.as_view(), name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<new_id>\d+)/comments/(?P<comment_id>\d+)$', views.comment_detail, name='comment_detail'),
    # ex: /polls/5/vote/
    url(r'^(?P<new_id>\d+)/comment$', views.comment, name='comment'),
)