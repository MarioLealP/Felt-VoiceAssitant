import socket
import os
import re
import server.protocolCodes as pC
from server.backend.backendConnection import start_server
from server.backend.backEndCommunication import receiveMessage, sendMessage

def mainServer():
    start_server()

    waitingForClientInput()


    #serverSocket.close()

def waitingForClientInput():
    waiting = True
    while waiting:
        try:
            data = receiveMessage()
            print(data)
            if(data != ""):
                sendMessage("I heard you say: " + data)
        except socket.timeout:
            print("No client connected")

if __name__ == "__main__":
    mainServer()
