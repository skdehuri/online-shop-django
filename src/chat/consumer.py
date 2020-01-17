from channels.consumer import AsyncConsumer


class ChatConsumer(AsyncConsumer):
    def connect(self, event):
        print('connected', event)

    def receive(self, event):
        print('receive', event)

    def disconnect(self, event):
        print('disconnected', event)
