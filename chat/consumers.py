import json
from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        print('---connect')

        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()


    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)


    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        print(text_data_json)
        message = text_data_json['message']

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    async def chat_message(self, event):
        message = event['message']

        await self.send(text_data=json.dumps({'message': message}))


# # synchronous style of consumer - needed if we use Django models in it
# class ChatConsumer(WebsocketConsumer):
    # def connect(self):
    #     self.room_name = self.scope['url_route']['kwargs']['room_name']
    #     self.room_group_name = 'chat_%s' % self.room_name

    #     async_to_sync(self.channel_layer.group_add)(self.room_group_name, self.channel_name)

    #     self.accept()

    # def disconnect(self, close_code):
    #     async_to_sync(self.channel_layer.group_discard)(self.room_group_name, self.channel_name)

    # def receive(self, text_data):
    #     text_data_json = json.loads(text_data)

    #     print(text_data_json)

    #     message = text_data_json['message']

    #     async_to_sync(self.channel_layer.group_send)(
    #         self.room_group_name,
    #         {
    #             'type': 'chat_message',
    #             'message': message
    #         }
    #     )

    # def chat_message(self, event):
    #     message = event['message']

    #     self.send(text_data=json.dumps({'message': message}))
