# -*- coding: utf-8 -*-
from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^movies/$', views.MovieListAPIView.as_view(), name='list'),
    url(r'^movies/(?P<pk>[0-9]+)/$', views.MovieAPIView.as_view(), name='movie-detail'),

    url(r'^rating/$', views.RatingCreateAPIView.as_view(), name='rating'),
    url(r'^rating/(?P<movie_id>[0-9]+)/$', views.RatingGetAPIView.as_view(), name='get'),
]
