from django.db import models
from django.core.validators import MinValueValidator
from Projection import Projection
from Seat import Seat


class Entry(models.Model):

    projection = models.ForeignKey(Projection, blank=False, null=False, on_delete=models.SET_NULL)
    seat = models.ForeignKey(Seat, blank=False, null=False, on_delete=models.SET_NULL)
    price = models.IntegerField(default=0, validators=[MinValueValidator(0)])

    def __str__(self):
        return str(self.projection) + str(self.seat)

    class Meta:
        unique_together = ["projection", "seat"]
