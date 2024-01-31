import socket
import settings
from server.client.clientCommunication import sendMessage
import server.client.socket as s



def start_client():
    # Create a TCP/IP socket
    s.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the server's address and port
    server_address = (settings.ServerIP, settings.ServerPort)
    s.clientSocket.connect(server_address)
    print("Connected to {}:{}".format(*server_address))

    try:
        # Send a string to the server
        message = "Client Connection"
        sendMessage(message)
        print("Sent message to server: {}".format(message))
        data = s.clientSocket.recv(1024)
        if(data.decode('utf-8') == "1"):
            print("Connection Successful")

        '''# Receive a file from the server
        file_path = 'received_file.txt'
        with open(file_path, 'wb') as file:
            file_data = s.clientSocket.recv(1024)
            while file_data:
                file.write(file_data)
                file_data = s.clientSocket.recv(1024)
            print("File received and saved as '{}'.".format(file_path))'''
    
    except Exception as e:
        print(e)

if __name__ == "__main__":
    start_client()
