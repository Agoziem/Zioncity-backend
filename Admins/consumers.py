# chat/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Notification
from .serializers import NotificationSerializer

class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print('connected')
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'notice_%s' % self.room_name
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()


    async def disconnect(self, close_code):
        # Leave room group
        print('disconnected')
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['notification']
        # update the database
        await self.update_notification(message)


    @database_sync_to_async
    def update_notification(self, message):
        try:
            notification = Notification.objects.get(id=message['id'])
            notification.users_seen.clear()
            notification.users_seen.add(*message['users_seen']) 
            notification.save()
        except Notification.DoesNotExist:
            pass
        except Exception as e:
            print(e)

    # Receive message from room group
    async def notification_message(self, event):
        notification = event['notification']
        action = event['action']

        await self.send(text_data=json.dumps({
            'action': action,
            'notification': notification
        }))