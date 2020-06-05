# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MaxValueValidator
from django.db.models import Avg


class Movie(models.Model):
    title = models.CharField(_('Movie\'s title'), max_length=255, unique=True)
    year = models.PositiveIntegerField(default=2019)
    # Example: PG-13
    rated = models.CharField(max_length=64)
    released_on = models.DateField(_('Release Date'))
    genre = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    plot = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse('movies:detail', kwargs={'id': self.pk})

    def get_rating(self):
        average = self.ratings.all().aggregate(Avg('rating'))['rating__avg']
        return average

class Rating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='ratings')
    rating = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(100)])
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.movie.title + u':' + str(self.rating)
