from django.db import models
from django.core.exceptions import ValidationError
from Hall import Hall
from Movie import Movie
from Time import Time


class Projection(models.Model):

    hall = models.ForeignKey(Hall, blank=False, null=False, on_delete=models.SET_NULL)
    movie = models.ForeignKey(Movie, blank=False, null=False, on_delete=models.SET_NULL)
    time = models.ForeignKey(Time, blank=False, null=False, on_delete=models.SET_NULL)

    def __str__(self):
        return self.movie.name + str(self.hall)

    def clean(self):
        if Projection.objects.filter(time=self.time, hall=self.hall).count() != 0:
            raise ValidationError("The same hall can't display more than one movie at the same time")

    class Meta:
        unique_together = [["hall", "movie"], ["hall", "time"], ["movie", "time"]]


