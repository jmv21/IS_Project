from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.http import JsonResponse
from django.shortcuts import render, redirect

from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.utils.decorators import method_decorator


class LoginFormView(LoginView):
    template_name = 'login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Welcome to Cinema+'
        return context
