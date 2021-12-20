import json
from django.shortcuts import render
from django.contrib.auth import get_user_model
from chat.models import ChatModel
from django.core import serializers

User = get_user_model()

# Create your views here.
def index(request):
    users = User.objects.exclude(username=request.user.username)
    return render(request, 'chat/index.html', context={'users': users})

def room(request, username):
    user_obj = User.objects.get(username=username)
    users = User.objects.exclude(username=request.user.username)

    if request.user.id > user_obj.id:
        room_name = f'chat_{request.user.id}-{user_obj.id}'
    else:
        room_name = f'chat_{user_obj.id}-{request.user.id}'
    print(room_name)

    messages_obj = serializers.serialize("json", ChatModel.objects.filter(room_name=room_name).order_by('timestamp'))
    messages = json.loads(messages_obj)
    print(messages)

    return render(request, 'chat/room.html', context={
        'user': user_obj,
        'users': users,
        'messages': messages
    })