from django.shortcuts import render_to_response

# Create your views here. 

def index(request):
    return render_to_response('dashboard/index.html', {'title': "Dashboard"})