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
from SnifferServer.sniffer import Sniffer


class SnifferConsumer(WebsocketConsumer):

    def connect(self):
        self.connection = True
        self.room_group_name = 'test'
        self.list = []
        self.sniffer = Sniffer("Wi-Fi", self.list)
        self.sniffer.start_sniffing()
        self.accept()
        self.index = 0
        print("connection started")
        print("#######################################")
        print(self.connection)

        self.stop = False  # A flag to break out from for loop
        # This thread will work same but
        self.thread = threading.Thread(target=self.action)
        # also allows to call disconnect()
        self.thread.start()

    def action(self):
        while self.connection == True:
            try:
                self.send(json.dumps(self.list[self.index]))
                self.index += 1
                time.sleep(0.1)
                if self.stop:
                    break
            except:
                pass

    def disconnect(self, code):
        self.stop = True
        del self.thread
        with open("sniffed_pkts.json", 'a') as file:
            file.write(']')
        print("connection closed")
        print("#######################################")
        print(self.connection)
        StopConsumer()
