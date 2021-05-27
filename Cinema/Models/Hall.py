from django.db import models


class Hall(models.Model):
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return "Hall #" + str(self.id)

