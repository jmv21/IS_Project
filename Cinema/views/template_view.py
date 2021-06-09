from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

from Cinema.forms import DiscountForm
from django.shortcuts import render
from django.forms import formset_factory
from django.views.generic import TemplateView

from Cinema.services.proyection_services import active_discounts_query, all_discounts_query, discount_update_active


class DiscountView(TemplateView):

    template_name = 'create_discount.html'
    success_url = reverse_lazy('home')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['discounts'] = all_discounts_query()
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return render(request, 'create_discount.html', context)
    
    def post(self, request, *args, **kwargs):

        try:
            options = request.POST.getlist('option[]')
        except:
            discount_update_active(None, True)
            return HttpResponseRedirect(self.success_url)

        discount_update_active(options)

        return HttpResponseRedirect(self.success_url)


class SelectDiscountView(TemplateView):
    template_name = 'select_discount.html'
    success_url = reverse_lazy('home')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['discounts'] = active_discounts_query()
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return render(request, 'select_discount.html', context)

    def post(self, request, *args, **kwargs):

        try:
            options = request.POST.getlist('option[]')
        except:
            options = ''

        discount_update_active(options)

        return HttpResponseRedirect(self.success_url)
