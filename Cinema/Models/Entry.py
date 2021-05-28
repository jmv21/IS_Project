from django.db import models
from django.core.validators import MinValueValidator
from .Projection import Projection
from .Seat import Seat


class Entry(models.Model):

    projection = models.ForeignKey(Projection, blank=False, null=True, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, blank=False, null=True, on_delete=models.SET_NULL)
    price = models.DecimalField(default=0.0, decimal_places=2, max_digits=10, validators=[MinValueValidator(0)])

    def __str__(self):
        return str(self.projection) + str(self.seat)

    class Meta:
        unique_together = ["projection", "seat"]
