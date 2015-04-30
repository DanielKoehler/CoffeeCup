from django.shortcuts import render_to_response
from django.shortcuts import render

from django.template import RequestContext
from django.contrib.auth.decorators import permission_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model

from django.http import JsonResponse, HttpResponse
from django.core import serializers

import json

from django.db.models import Q

User = get_user_model()

@permission_required('useradminstration.can_view')
def user_list(request):

    objs = User.objects.filter(~Q(id =request.user.id), is_staff = True)

    return JsonResponse([x.as_json() for x in objs], safe=False)
