from django.template import loader
from django.http import HttpResponse

from Cinema.models.Hall import Seat


def home(request):
    # <--Load the template--->
    template = loader.get_template('Main_Templates/base.html')
    return HttpResponse(template.render({}, request))


def reserves(request):
    template = loader.get_template('reserve.html')
    result = Seat.objects.all()

    context = {
        'seats': result
    }
    return HttpResponse(template.render(context, request))


