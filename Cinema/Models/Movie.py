from django.db import models
from django.core.validators import MinValueValidator



class Movie(models.Model):

    name = models.CharField(max_length=50)

    nationality = models.CharField(max_length=50)

    genre = models.CharField(max_length=50)

    views = models.IntegerField(default=0,validators=[MinValueValidator(0)])

    likes = models.IntegerField(default=0, validators=[MinValueValidator(0)])

    poster = models.ImageField(default='/profile_pics/default.jpg', upload_to='profile_pics/', null=False, blank=False)

    synopsis = models.TextField(default="It's a movie", max_length=250)

    def __str__(self):
        return self.name

