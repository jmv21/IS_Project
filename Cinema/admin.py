from django.contrib import admin
from .models.Actor import Actor, Movie, Discount
from .models.Projection import Projection
from .models.Hall import Hall, Seat
from .models.Entry import Entry
from .models.Purchase import Purchase
from .models.Time import Time


# Register your models here.
class CinemaAdmin(admin.ModelAdmin):
    def has_delete_permission(self, request, obj=None):
        return False
    def has_add_permission(self, request):
        return False
    def has_change_permission(self, request, obj=None):
        return False

admin.site.register(Actor)
admin.site.register(Hall)
admin.site.register(Seat, CinemaAdmin)
admin.site.register(Time)
admin.site.register(Projection)
admin.site.register(Movie)
admin.site.register(Entry)
admin.site.register(Discount)
admin.site.register(Purchase)
