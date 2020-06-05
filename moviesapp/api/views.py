# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import generics
from django.db.models import Avg

import serializers

from moviesapp.movies.models import Movie, Rating

class MovieListAPIView(generics.ListCreateAPIView):
    queryset = Movie.objects.all().annotate(avg_rating=Avg('ratings__rating'))
    serializer_class = serializers.MovieListSerializer

class MovieAPIView(generics.RetrieveAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = Movie.objects.all().annotate(avg_rating=Avg('ratings__rating'))
    serializer_class = serializers.MovieSerializer

class RatingCreateAPIView(generics.CreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = serializers.RatingSerializer
