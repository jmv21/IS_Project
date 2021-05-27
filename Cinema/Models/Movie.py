from django.db import models
from django.core.validators import MinValueValidator
from Actor import Actor


class Movie(models.Model):

    name = models.CharField(max_length=50)

    nationality = models.CharField(max_length=50)

    genre = models.CharField(max_length=50)

    views = models.IntegerField(default=0,validators=[MinValueValidator(0)])

    likes = models.IntegerField(default=0, validators=[MinValueValidator(0)])

    poster = models.ImageField()

    synopsis = models.TextField()

    cast = models.ForeignKey(Actor, blank=False, null=False, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

