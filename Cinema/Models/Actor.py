from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from Movie import Movie


class Actor(models.Model):

    name = models.CharField(max_length=50)
    movie = models.ForeignKey(Movie, blank=False, null=False, on_delete=models.SET_NULL)
    age = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(150)])
    sex = models.CharField(max_length=50)
    photo = models.ImageField()

    def __str__(self):
        return self.name
