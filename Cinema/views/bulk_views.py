from django.shortcuts import render

# Home page view
from django.views.generic import ListView

from Cinema.services import proyection_services

from Cinema.models.Actor import Actor
from Cinema.models.Movie import Movie
from Cinema.models.Projection import Projection






class MoviesListView(ListView):
    model = Movie
    template_name = 'movies.html'
    paginate_by = 2

    def get_queryset(self):
        return proyection_services.movies_query()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Movie Catalog'
        return context


def actors(request):
    actors = proyection_services.actors_query()

    context = {
        'actors': actors
    }
    return render(request, 'Actors.html', context)


class ActorsListView(ListView):
    model = Actor
    template_name = 'Actors.html'
    paginate_by = 2

    def get_queryset(self):
        return proyection_services.actors_query()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Actors'
        return context


def projections(request):
    projections = proyection_services.projection_query()

    context = {
        'projections': projections
    }
    return render(request, 'Projections.html', context)


class ProjectionsListView(ListView):
    model = Projection
    template_name = 'Projections.html'
    paginate_by = 2

    def get_queryset(self):
        return proyection_services.projection_query()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Projections'

        return context

