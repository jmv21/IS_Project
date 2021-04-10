from django import template

from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView

from Cinema.models.Entry import Entry
from Cinema.models.Hall import Seat

from Cinema.services.proyection_services import get_spec_proj, seats_query
from Cinema.services.proyection_services import seats_query, get_spec_proj
from Cinema.models.Purchase import Purchase

from Cinema.services.proyection_services import get_spec_proj, seats_query

from Cinema.services.proyection_services import seats_query, get_spec_proj



def home(request):
    # <--Load the template--->
    template = loader.get_template('Main_Templates/base.html')
    return HttpResponse(template.render({}, request))


def test(request):
    # <--Load the template--->
    template = loader.get_template('test.html')
    return HttpResponse(template.render({}, request))


    def get(self, request, *args, **kwargs):
        proj_id = self.kwargs['hall']
        self.projection = proj_id
        proj = get_spec_proj(proj_id)
        context = self.get_context_data(**kwargs)
        context['projection'] = proj
        context['seats'] = seats_query(proj.hall_id)
        return render(request, self.template_name, context)

        context['proj'] = proj
        context['seats'] = seats_query(proj.hall_id)
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):

        try:
            options = request.POST.getlist('option[]')
        except:
            return HttpResponseRedirect(reverse_lazy('home'))

        # Create an entry for every selected seat
        entries_list = []
        for seat in options:
            aux = Entry.create(self.projection, seat)
            entries_list.append(aux)
            aux.save(*args, **kwargs)

        email = request.POST['email']

        # NEEDED FOR THE NEXT STEP
        purchase = Purchase.create(email=email, entries=entries_list)
        Purchase.save()

        return HttpResponseRedirect(self.success_url)

