from django.contrib import admin
from .Models.Actor import Actor, Movie
from .Models.Projection import Projection
from .Models.Seat import Seat, Hall
from .Models.Entry import Entry
from .Models.Time import Time

# Register your models here.
admin.site.register(Actor)
admin.site.register(Hall)
admin.site.register(Time)
admin.site.register(Projection)
admin.site.register(Seat)
admin.site.register(Movie)
admin.site.register(Entry)
