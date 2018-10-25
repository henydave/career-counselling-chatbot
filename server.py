# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 14:42:22 2018

@author: henyd
"""

from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
from chatbot_final2 import get_response


class ChatServer(WebSocket):

    def handleMessage(self):
        # echo message back to client
        message = self.data
        response = get_response(message)
        self.sendMessage(response)

    def handleConnected(self):
        print(self.address, 'connected')

    def handleClose(self):
        print(self.address, 'closed')



server = SimpleWebSocketServer('', 8000, ChatServer)
server.serveforever()
