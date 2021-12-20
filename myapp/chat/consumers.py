# chat/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from chat.models import ChatModel
from channels.db import database_sync_to_async

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        logged_in_user_id = self.scope['user'].id
        other_user_id = self.scope['url_route']['kwargs']['id']

        # Alphabetical order
        if int(logged_in_user_id) > int(other_user_id):
            self.room_name = f'{logged_in_user_id}-{other_user_id}'
        else:
            self.room_name = f'{other_user_id}-{logged_in_user_id}'

        self.room_group_name = 'chat_%s' % self.room_name
        
        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()
        
    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        username = text_data_json['username']

        print(username, message, self.room_group_name)
        # Save the message
        await self.save_message(username, message, self.room_group_name)

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': username
            },
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        username = event['username']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'username': username
        }))

    @database_sync_to_async
    def save_message(self, username, message, room_name):
        ChatModel.objects.create(sender=username, message=message, room_name=room_name)