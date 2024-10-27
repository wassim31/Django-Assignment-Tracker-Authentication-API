import json
from channels.generic.websocket import AsyncWebsocketConsumer

class AssignmentConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = 'assignment_updates'
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def send_assignment_update(self, event):
        assignment_data = event['data']
        await self.send(text_data=json.dumps({
            'type': 'assignment_update',
            'data': assignment_data
        }))
