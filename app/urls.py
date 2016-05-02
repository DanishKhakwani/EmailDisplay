from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    #url(r'^(?P<user_id>[A-Za-z0-9]+/$)', views.search, name='search'),
    url(r'^search/$', views.search, name='search'),
    url(r'^(?P<email_id>[0-9]+)/$', views.detail, name='detail'),
]
