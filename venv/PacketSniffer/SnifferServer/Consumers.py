import json
from channels.generic.websocket import WebsocketConsumer
from channels.exceptions import StopConsumer
# from channels.exceptions import StopConsumer
# from asgiref.sync import async_to_sync
# import time
# import threading
class SnifferConsumer(WebsocketConsumer):
      stop = False
      connection = True

      def connect(self):
        self.accept()
        print("connection established")
        print("#######################")

        self.send(text_data=json.dumps({
            'type':'connection established',
            'msg':'you are now connected!'
        }))
      
      def disconnect(self, code):
         self.stop = True
         # del self.thread
         print("connection closed")
         print("#######################################")
         print(self.connection)
         StopConsumer()