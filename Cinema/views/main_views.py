<<<<<<< HEAD
=======
from django import template
>>>>>>> 972da751cb85698ba61a880221e3ed75b3e4abb3
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView

from Cinema.models.Hall import Seat
<<<<<<< HEAD
from Cinema.services.proyection_services import get_spec_proj, seats_query
=======
from Cinema.services.proyection_services import seats_query, get_spec_proj
>>>>>>> 972da751cb85698ba61a880221e3ed75b3e4abb3


def home(request):
    # <--Load the template--->
    template = loader.get_template('Main_Templates/base.html')
    return HttpResponse(template.render({}, request))


class Reserves(TemplateView):
    template_name = 'reserve.html'
    success_url = reverse_lazy('home')

    def __init__(self, **kwargs):
        projection = None
        super().__init__(**kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

<<<<<<< HEAD
class Reserves(TemplateView):
    template_name = 'reserve.html'
    success_url = reverse_lazy('home')

    def __init__(self, **kwargs):
        projection = None
        super().__init__(**kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

=======
>>>>>>> 972da751cb85698ba61a880221e3ed75b3e4abb3
    def get(self, request, *args, **kwargs):
        proj_id = self.kwargs['hall']
        self.projection = proj_id
        proj = get_spec_proj(proj_id)
        context = self.get_context_data(**kwargs)
<<<<<<< HEAD
        context['proj'] = proj
        context['seats'] = seats_query(proj.hall_id)
        return render(request, self.template_name, context)

=======
        context['projection'] = proj
        context['seats'] = seats_query(proj.hall_id)
        return render(request, self.template_name, context)
>>>>>>> 972da751cb85698ba61a880221e3ed75b3e4abb3
