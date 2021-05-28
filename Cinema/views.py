from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse


# Home page view
def home(request):
    # <--Load the template--->
    template = loader.get_template('Main_Templates/base.html')

    return HttpResponse(template.render({}, request))
