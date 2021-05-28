from django.contrib import admin
from .models.Actor import Actor, Movie
from .models.Projection import Projection
from .models.Seat import Seat, Hall
from .models.Entry import Entry
from .models.Time import Time

# Register your models here.
admin.site.register(Actor)
admin.site.register(Hall)
admin.site.register(Time)
admin.site.register(Projection)
admin.site.register(Seat)
admin.site.register(Movie)
admin.site.register(Entry)
