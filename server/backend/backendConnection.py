import socket
import os
import re
import server.protocolCodes as pC
import server.backend.socket as s
from server.backend.backEndCommunication import receiveMessage, sendMessage

def start_server():
    # Create a TCP/IP socket
    s.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to a specific address and port
    server_address = ('localhost', 8520)
    s.serverSocket.bind(server_address)

    # Listen for incoming connections
    s.serverSocket.listen(1)
    print("Server is listening on {}:{}".format(*server_address))

    while True:
        # Wait for a connection
        print("Waiting for a connection...")
        s.clientSocket, client_address = s.serverSocket.accept()
        print("Connection established with {}".format(client_address))

        try:
            # Receive data from the client
            data = receiveMessage()
            print("Socket: " + str(s.clientSocket))
            if(re.search("Client Connection", data)):
                print("Client Connection")
                sendMessage(pC.success)
                return s.clientSocket
        
        except Exception as e:
            print(e)
