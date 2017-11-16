from django.conf.urls import url
from . import views #this line is new! #imports views.py from current folder
urlpatterns=[
    url(r'^$', views.index),#this line has changed!,
    url(r'^(?P<id>\d+)$', views.show),#if post, calls views.update to update
    url(r'^(?P<id>\d+)/edit$', views.edit),
    url(r'^new$', views.new),
    url(r'^create$', views.create),
    url(r'^(?P<id>\d+)/destroy$', views.destroy),
]
