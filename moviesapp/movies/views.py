# -*- coding: utf-8 -*-

"""Movies views."""

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.shortcuts import redirect
from django.http import Http404
from django.urls import reverse_lazy

from .models import Movie, Rating
from django.db.models import Avg

class MovieListView(ListView):
    """Show all movies."""
    model = Movie

    def get_queryset(self):
        sort = self.request.GET.get('sort', 'released')
        order_by = '-released_on'
        if (sort == 'rating'):
            order_by = '-avg_rating'
        return Movie.objects.all().annotate(avg_rating=Avg('ratings__rating')).order_by(order_by)

class MovieDetailView(DetailView):
    """Show the requested movie."""
    model = Movie
    pk_url_kwarg = 'id'

class MovieCreateView(SuccessMessageMixin, CreateView):
    """Create a new movie."""
    model = Movie
    fields = ('__all__')
    success_message = 'The movie created successfully'
    error_message = 'The creation has failed'

    def form_invalid(self, form):
        response = super(MovieCreateView, self).form_invalid(form)
        messages.error(self.request, self.error_message)
        return response


class MovieUpdateView(SuccessMessageMixin, UpdateView):
    """Update the requested movie."""
    model = Movie
    fields = ('__all__')
    pk_url_kwarg = 'id'
    success_message = 'The movie updated successfully'
    error_message = 'The update has failed'

    def form_invalid(self, form):
        response = super(MovieUpdateView, self).form_invalid(form)
        messages.error(self.request, self.error_message)
        return response


class MovieDeleteView(DeleteView):
    """Delete the requested movie."""
    model = Movie
    success_url = reverse_lazy('movies:index')
    pk_url_kwarg = 'id'
    success_message = 'The movie deleted successfully'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(MovieDeleteView, self).delete(request, *args, **kwargs)

class MovieRateCreateView(SuccessMessageMixin, CreateView):
    """Create new rating"""
    model = Rating
    fields = ('__all__')
    success_url = reverse_lazy('movies:index')
    success_message = 'The rating created successfully'
    error_message = 'The creation has failed'

    def form_invalid(self, form):
        response = super(MovieRateCreateView, self).form_invalid(form)
        messages.error(self.request, self.error_message)
        return response

    def get_initial(self):
        return {
                'movie': get_object_or_404(Movie, pk=self.kwargs['mid']),
                }
