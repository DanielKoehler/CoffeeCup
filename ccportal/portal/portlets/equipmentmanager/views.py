from django.shortcuts import render_to_response
from django.shortcuts import render

from django.template import RequestContext
from django.contrib.auth.decorators import permission_required

# Create your views here. 

@permission_required('equipmentmanager.can_view', login_url='/login/')
def index(request):
    return render(request, 'equipmentmanager/index.html', {'title': "Equipment Manager"})