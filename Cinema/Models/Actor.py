from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from .Movie import Movie


class Actor(models.Model):

    name = models.CharField(max_length=50)
    movie = models.ForeignKey(Movie, blank=False, null=True, on_delete=models.SET_NULL)
    age = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(120)])
    sex = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='media')

    def __str__(self):
        return self.name
