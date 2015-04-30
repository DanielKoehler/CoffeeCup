from django.shortcuts import render_to_response
from django.shortcuts import render

from django.template import RequestContext
from django.contrib.auth.decorators import permission_required
from django.views.decorators.csrf import csrf_exempt

from django.http import JsonResponse, HttpResponse
from django.core import serializers

from models import Directory, File

import json, re

from itertools import chain

from forms import DirectoryForm

# Create your views here. 
@permission_required('mediasharing.can_view')
def get_base(request):

    x = Directory.objects.filter(parent__isnull=True, owner__id=request.user.id)
    y = File.objects.filter(parent__isnull=True, owner__id=request.user.id)

    return JsonResponse({'name':None,'files':[z.get_client_inode() for z in chain(x, y)]}, safe=False)


# Create your views here. 
@permission_required('mediasharing.can_view')
def get_directory(request, objectId):
    return JsonResponse(Directory.objects.filter(id=objectId, owner__id=request.user.id).first().get_client_inode(), safe=False)

# Create your views here. 
@permission_required('mediasharing.can_create')
def post_directory(request):

    data = json.loads(request.body)

    if all (key in data for key in ("name", "parent")):

        name = data['name']
        parent = Directory.objects.get(id=data['parent']) if type(data['parent']) is int else None; 

        directory = Directory(name=name, parent=parent, owner=request.user, bytes=0)
        
        directory.save()

        return JsonResponse(directory.get_client_inode(), safe=False)

    return JsonResponse({'message':'Invalid post data..'}, status=400, safe=False)

# Create your views here. 
@permission_required('mediasharing.can_create')
def post_directory_rename(request, objectId):

    objectId = re.sub("[^0-9]", "", objectId)

    data = json.loads(request.body)

    if "name" in data:

        d = Directory.objects.get(id=objectId)

        d.name = data['name']
        
        d.save()

        return JsonResponse(d.get_client_inode(), safe=False)

    return JsonResponse({'message':'Invalid post data..'}, status=400, safe=False)

@permission_required('mediasharing.can_create')
def post_file_rename(request, objectId):

    objectId = re.sub("[^0-9]", "", objectId)

    data = json.loads(request.body)

    if "name" in data:

        f = File.objects.get(id=objectId)

        f.name = data['name']
        
        f.save()

        return JsonResponse(d.get_client_inode(), safe=False)

    return JsonResponse({'message':'Invalid post data..'}, status=400, safe=False)

@permission_required('mediasharing.can_view')
def get_object(request, objectId):

    objs = File.objects.filter(parent__isnull=True, owner__id=request.user.id)
    data = serializers.serialize("json", Directory.objects.filter(parent__isnull=True, owner__id=request.user.id))

    return JsonResponse(data, safe=False)

@permission_required('mediasharing.can_view')
def serve_object(request, objectId):

    objectId = re.sub("[^0-9]", "", objectId)

    object_name = File.objects.get(id=objectId)
    
    filename = object_name.file.name.split('/')[-1]
    response = HttpResponse(object_name.file, content_type=object_name.mime)
    response['Content-Disposition'] = 'attachment; filename=%s' % filename

    return response

@permission_required('mediasharing.can_create')
def post_object(request):

    if request.method == "POST":

        upload = request.FILES['file']
        parent = request.POST.get('parent') if 'parent' in request.POST.keys() else None

        f = File(name=upload.name, file=upload, owner=request.user, parent=parent, bytes=request.POST.get('size'), mime=request.POST.get('type'))
        f.save()

        return JsonResponse(f.get_client_inode(), safe=False)
    return JsonResponse({'message':'Invalid file..'}, status=400, safe=False)

@permission_required('mediasharing.can_delete')
def delete_object(request):

    data = json.loads(request.body)    
    removed_set = []

    if "objects" in data:
        print data['objects']
        for obj in data['objects']:
            parts = re.compile("^(d|f){1}([0-9]+)$").split(obj)
            print parts
            if parts[1] == 'd':
                Directory.objects.get(id=parts[2]).delete()
                removed_set.append(obj)
            elif parts[1] == 'f':
                File.objects.get(id=parts[2]).delete()
                removed_set.append(obj)

        return JsonResponse(removed_set, safe=False)

    return JsonResponse({'message':'No objects..'}, status=400)
