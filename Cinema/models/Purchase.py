from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from Cinema.models.Actor import Discount
from Cinema.models.Entry import Entry
from Cinema.models.Hall import Seat


class Purchase(models.Model):

    email = models.EmailField()
    entries = models.ManyToManyField(Entry,blank=False, null=False)
    # A list of discounts id separated by ','
    discounts = models.ManyToManyField(Discount)

    def __str__(self):
        return str(self.email) + " reservation"

    @classmethod
    def create(cls, email, entries, discounts=None):
        purchase = cls(email=email, entries=entries, discounts=discounts)
        return purchase
