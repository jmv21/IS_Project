from django.db import models
from django.core.exceptions import ValidationError


class Time(models.Model):

    beginning_time = models.DateTimeField()
    ending_time = models.DateTimeField()

    def __str__(self):
        return f"starts at {self.beginning_time} and ends at {self.ending_time}"

    def clean(self):
        if self.ending_time <= self.beginning_time:
            raise ValidationError("Ending time can't be less or equal to beginning time")


