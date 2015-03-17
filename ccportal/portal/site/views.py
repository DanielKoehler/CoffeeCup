from forms import LoginForm
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout

def user_login(request):

    logout(request)
    username = password = ''

    if request.POST:

        username = request.POST['email']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/dashboard')
            else:
                pass
                # Return a 'disabled account' error message
        else:
            pass
            # Return an 'invalid login' error message.

    form = LoginForm()

    return render(request, 'site/login.html', {'title': 'Login', 'form': form})

def user_logout(request):

    logout(request)
    
    return HttpResponseRedirect('/login/')
