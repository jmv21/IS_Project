from Cinema.models.Actor import Actor
from Cinema.models.Movie import Movie
from Cinema.models.Projection import Projection


def actors_query():

    return Actor.objects.all()


def movies_query():

    return Movie.objects.all()


def projection_query():

    return Projection.objects.all()
