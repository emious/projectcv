import json
from channels.generic.websocket import AsyncWebsocketConsumer


class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Called when the websocket is handshaking as part of the connection process.
        await self.accept()

    async def disconnect(self, close_code):
        # Called when the WebSocket closes.
        pass

    async def receive(self, text_data):
        # Called when the server receives a message from WebSocket.
        text_data_json = json.loads(text_data)
        message = text_data_json.get('message', '')

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))

    async def send_notification(self, event):
        # Called when the server sends a message to the WebSocket.
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))
