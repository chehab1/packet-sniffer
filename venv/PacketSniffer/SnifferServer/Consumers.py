# consumers are the channels versions of django views
# they do more than request/response
# they can innitiate request while keeping connection

import json
from channels.generic.websocket import WebsocketConsumer
from channels.exceptions import StopConsumer
from asgiref.sync import async_to_sync
import time
import threading
import random

def fn():
   f = open(r"D:\00-GitHub\Packet-Sniffer\packet-sniffer\venv\PacketSniffer\SnifferServer\data.json")
   data = json.load(f)
   f.close()
   return data


class SnifferConsumer(WebsocketConsumer):

   def connect(self):
      self.connection = True
      self.room_group_name = 'test'

      self.accept()

      print("connection started")
      print("#######################################")
      print(self.connection)

      self.stop = False  # A flag to break out from for loop
      self.thread = threading.Thread(target=self.action)  # This thread will work same but 
      self.thread.start()                                 # also allows to call disconnect()

   
   def action(self):
      while self.connection == True:
         data = fn()
         print(data[-1])
         self.send(text_data=json.dumps(data[-1]))
         time.sleep(3)
         if self.stop:
            break

   def disconnect(self, code):
      self.stop = True
      del self.thread
      print("connection closed")
      print("#######################################")
      print(self.connection)
      StopConsumer()
        