from django.contrib.auth import logout
from django.contrib.auth.views import LoginView, LogoutView
from  django.utils.decorators import method_decorator
from d
from django.shortcuts import render, redirect
from django.views.generic import RedirectView

from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.utils.decorators import method_decorator


class LoginFormView(LoginView):
    template_name = 'login.html'

    @method_decorator(sensitive_post_parameters())
    def dispatch(self, request, *args, **kwargs):
        if(request.user.is_authenticated):
            return redirect('/')
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Welcome to Cinema+'
        return context

class LogoutRedirectView(RedirectView):
    pattern_name = 'home'

    def dispatch(self, request, *args, **kwargs):
        logout(request)
        return super().dispatch(request, *args, **kwargs)
