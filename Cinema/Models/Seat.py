from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from .Hall import Hall


class Seat(models.Model):
    number = models.IntegerField(validators=[MinValueValidator(0)])
    hall = models.ForeignKey(Hall, blank=False, null=True, on_delete=models.CASCADE)
    reserved = models.BooleanField(blank=False, null=False)

    def __str__(self):
        return "Seat # " + str(self.number) + " hall " + str(self.hall.id)

    def clean(self):
        if Seat.objects.filter(number=self.number, hall=self.hall).count() != 0:
            raise ValidationError("Can't be two seats with the same number in the same hall")

