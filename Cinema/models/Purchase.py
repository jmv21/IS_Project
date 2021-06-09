from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from Cinema.models.Entry import Entry
from Cinema.models.Hall import Seat


class Purchase(models.Model):

    email = models.EmailField()
    entry = models.ForeignKey(Entry, blank=False, null=False, on_delete=models.SET_NULL)
    seat = models.ForeignKey(Seat, blank=False, null=False, on_delete=models.SET_NULL)
    # A list of discounts id separated by ','
    discounts = models.CharField(max_length=100)

    def __str__(self):
        return str(self.entry) + " reserved"
