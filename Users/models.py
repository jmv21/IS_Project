from django.core.validators import MinValueValidator
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.forms import model_to_dict

from IS_Project.settings import MEDIA_URL, STATIC_URL


class Profile(AbstractUser):
    partner_points = models.DecimalField(validators=[MinValueValidator(0)], default=0, null=False, decimal_places=2, max_digits=10)
    image = models.ImageField(default='/profile_pics/default.jpg', upload_to='profile_pics/', null=True, blank=True)

    def get_image(self):
        if self.image:
            return '{}{}'.format(MEDIA_URL, self.image)
        return '{}{}'.format(STATIC_URL, 'media/default.jpg')

    def toJSON(self):
        item = model_to_dict(self, exclude=['password', 'groups', 'user_permissions', 'last_login'])
        if self.last_login:
            item['last_login'] = self.last_login.strftime('%Y-%m-%d')
        item['date_joined'] = self.date_joined.strftime('%Y-%m-%d')
        item['image'] = self.get_image()
        return item

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
