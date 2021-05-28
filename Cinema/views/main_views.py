from django.template import loader
from django.http import HttpResponse

def home(request):
    # <--Load the template--->
    template = loader.get_template('Main_Templates/base.html')

    return HttpResponse(template.render({}, request))
