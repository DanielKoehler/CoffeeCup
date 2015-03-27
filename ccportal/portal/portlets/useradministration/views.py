from django.shortcuts import render_to_response
from django.shortcuts import render

from django.template import RequestContext
from django.contrib.auth.decorators import permission_required

# Create your views here. 
@permission_required('useradministration.can_view', login_url='/login/')
def users(request):
    return render(request, 'useradministration/index.html', {'title': 'User Administration'})

@permission_required('useradministration.can_view', login_url='/login/')
def groups(request):
    return render(request, 'useradministration/index.html', {'title': 'User Administration'})

