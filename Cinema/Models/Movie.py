from django.db import models
from django.core.validators import MinValueValidator



class Movie(models.Model):

    name = models.CharField(max_length=50)

    nationality = models.CharField(max_length=50)

    genre = models.CharField(max_length=50)

    views = models.IntegerField(default=0,validators=[MinValueValidator(0)])

    likes = models.IntegerField(default=0, validators=[MinValueValidator(0)])

    poster = models.ImageField()

    synopsis = models.TextField()

    def __str__(self):
        return self.name

