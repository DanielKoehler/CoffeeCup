from django.shortcuts import render_to_response
from django.shortcuts import render

from django.template import RequestContext
from django.contrib.auth.decorators import permission_required
from django.views.decorators.csrf import csrf_exempt

from django.http import JsonResponse, HttpResponse
from django.core import serializers

from models import Event 

import json, re

from itertools import chain


# Create your views here. 
@permission_required('scheduler.can_view')
def get_events(request):

    events = request.user.event_set.all()

    return JsonResponse([x.as_json() for x in events], safe=False)


# Create your views here. 
@permission_required('scheduler.can_view')
def get_directory(request, objectId):
    return JsonResponse(Directory.objects.filter(id=objectId, owner__id=request.user.id).first().get_client_inode(), safe=False)
