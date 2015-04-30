from django.shortcuts import render_to_response
from django.shortcuts import render
from django.core.urlresolvers import reverse

from django.template import RequestContext
from django.contrib.auth.decorators import permission_required

# Create your views here. 
@permission_required('dashboard.can_view', login_url='/login/')
def index(request):
    context = RequestContext(request,
                           {'request': request,
                            'user': request.user})
    return render(request, 'dashboard/index.html', {'title': "Dashboard"}, context_instance=context)