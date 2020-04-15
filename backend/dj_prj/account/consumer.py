import json
from channels.generic.websocket import WebsocketConsumer

class OnlineConsumer(WebsocketConsumer):
    def connect(self):
        print('websocket connecting')
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        print(text_data_json)