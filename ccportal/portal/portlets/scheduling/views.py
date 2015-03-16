from django.shortcuts import render_to_response
from django.shortcuts import render

from django.template import RequestContext

# Create your views here. 

def index(request):
    return render(request, 'scheduling/index.html', {'title': "Scheduling"})