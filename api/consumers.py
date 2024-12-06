import json
from channels.generic.websocket import AsyncWebsocketConsumer

class AlertConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Добавляем соединение в группу 'alerts'
        await self.channel_layer.group_add(
            "alerts",
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # Удаляем соединение из группы 'alerts'
        await self.channel_layer.group_discard(
            "alerts",
            self.channel_name
        )

    # Метод, который будет вызываться при получении сообщения из группы
    async def alert_message(self, event):
        message = event['message']
        # Отправляем сообщение на фронтенд
        await self.send(text_data=json.dumps(message))
