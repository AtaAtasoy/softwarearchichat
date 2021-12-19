import json
from django.shortcuts import render
from django.core import serializers
from chat.models import ChatModel


# Create your views here.
def index(request):
    return render(request, 'chat/index.html')

def room(request, room_name):
    messages = serializers.serialize("json", ChatModel.objects.filter(room_name=room_name).order_by('timestamp'))
    messages_obj = json.loads(messages)

    return render(request, 'chat/room.html', {
        'room_name': room_name,
        'messages': messages_obj
    })