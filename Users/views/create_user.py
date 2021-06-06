from django.contrib.auth import login, authenticate
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView

from Users.forms import UserForm
from Users.models import Profile


class UserCreateView(CreateView):
    model = Profile
    form_class = UserForm
    template_name = 'register.html'
    success_url = reverse_lazy('home')

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        valid = super().form_valid(form)
        username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password')
        new_user = authenticate(username=username, password=password)
        login(self.request, new_user)
        return valid

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'add'
        context['success_url'] = self.success_url
        return context
