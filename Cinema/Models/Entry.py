from django.db import models
from django.core.validators import MinValueValidator
from .Projection import Projection
from .Hall import Seat


class Entry(models.Model):

    projection = models.ForeignKey(Projection, blank=False, null=True, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, blank=False, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.projection) + str(self.seat)

    class Meta:
        unique_together = ["projection", "seat"]

    @classmethod
    def create(cls, projection, seat):

        entry = cls(projection=projection, seat=seat)
        return entry
