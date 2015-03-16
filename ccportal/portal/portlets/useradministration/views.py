from django.shortcuts import render_to_response
from django.shortcuts import render

from django.template import RequestContext

# Create your views here. 

def users(request):
    return render(request, 'useradministration/index.html', {'title': 'User Administration'})

def groups(request):
    return render(request, 'useradministration/index.html', {'title': 'User Administration'})
