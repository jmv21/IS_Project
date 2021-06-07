from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models


class Hall(models.Model):
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return "Hall #" + str(self.id)

    def save(self, *args, **kwargs):
        created = not self.pk
        super().save(*args, **kwargs)
        if created:
            batch_size = 20
            objs = (Seat(number=i + 1, hall=self, reserved=False) for i in range(20))
            Seat.objects.bulk_create(objs, batch_size)


class Seat(models.Model):
    number = models.IntegerField(validators=[MinValueValidator(0)])
    hall = models.ForeignKey(Hall, blank=False, null=False, on_delete=models.CASCADE)
    reserved = models.BooleanField(blank=False, null=False, default=False)

    def __str__(self):
        return "Seat # " + str(self.number) + " hall " + str(self.hall.id)

    def clean(self):
        if Seat.objects.filter(number=self.number, hall=self.hall).count() != 0:
            raise ValidationError("Can't be two seats with the same number in the same hall")

    class Meta:
        ordering = ['id']
