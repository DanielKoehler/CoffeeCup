from django.shortcuts import render
from django.http import HttpResponse, HttpResponseServerError
from django.views.decorators.csrf import csrf_exempt
from django.contrib.sessions.models import Session
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

from django.forms.models import model_to_dict


import json

from models import Thread, Message
from sockjs.tornado import SockJSConnection

User = get_user_model()



class MessengerConnection(SockJSConnection):

    _connected = set()

    def get_user(self, request):

        session = Session.objects.get(session_key=request.get_cookie('sessionid').value)
        user_id = session.get_decoded().get('_auth_user_id')

        return User.objects.get(id=user_id)

    def on_open(self, request):
        
        self.user = self.get_user(request)
        self._connected.add(self)

        for thread in self.user.thread_set.all().order_by('last_message')[:5]:
            messages = [self._package_message(m) for m in thread.message_set.all().order_by('date')[:10]]
            self.send({
                'route':'thread',
                'data': self._package_thread(thread, messages)
                })

    def on_message(self, data):
        
        data = json.loads(data)

        if 'event' not in data:
            return

        options = {
            'addMessage' : self.addMessage,
            'addThread' : self.addThread,
        }

        return options[data['event']](data)



    def addMessage(self, data):

        if 'message' not in data:
            return

        message = data['message'].strip()
        thread = Thread.objects.get(id=data['thread'])

        # Is valid message?
        if not len(message) or thread is None:
            return

        msg = Message.objects.create(
            user = self.user,
            text = data['message'],
            thread = thread
        )

        msg.save()

        self.broadcast(self._connected, {
            'route':'message',
            'data':self._package_message(msg)
            })

    def addThread(self, data):

        if 'users' not in data:
            return

        data['users'].append(self.user.id)

  

        users = User.objects.filter(id__in=data['users'])
            
        t = Thread.objects.create(active=True)

        print t

        for user in users:
            t.users.add(user)

        return self.broadcast(self._connected, {
            'route':'thread',
            'data':self._package_thread(t)
            })


    def on_close(self):
        self._connected.remove(self)

    def jsonify_user(self, user):
        return {
                'id':user.id,
                'first_name': user.first_name, 
                'last_name': user.last_name,
                'full_name': user.get_full_name(),
                'avatar': user.get_avatar, #MAKE DYNAMIC IN USER MODEL.
                'email':user.email
                }

    def _package_message(self, m):
        return  {
                    'user':self.jsonify_user(m.user),
                    'thread': m.thread.id,
                    'datetime': m.date.strftime('%H:%M:%S'),
                    'text': m.text,
                    'id': m.id
                }
            

    def _package_thread(self, thread, recent_messages = []):
        return {
                    'id':thread.id, 
                    'users':[self.jsonify_user(user) for user in thread.users.all() if user.id is not self.user.id], 
                    'image':None, 
                    'last_message':None,
                    'messages':recent_messages,
                }


