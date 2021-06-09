from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from .Movie import Movie


class Actor(models.Model):

    name = models.CharField(max_length=50)
    movie = models.ForeignKey(Movie, blank=False, null=True, on_delete=models.SET_NULL)
    age = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(120)])
    photo = models.ImageField(upload_to='media')

    def __str__(self):
        return self.name


class Discount(models.Model):

    type = models.CharField(null=False, blank=False, max_length=50)
    amount = models.IntegerField(null=False, blank=False, validators=[MinValueValidator(0), MaxValueValidator(100)])
    description = models.TextField(null=False, blank=False)
    active = models.BooleanField()

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = 'Discount'
