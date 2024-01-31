import server.client.socket as s

def sendMessage(message):
    message = "C: " + message
    s.clientSocket.send(message.encode('utf-8'))

def receiveMessage():
    data = s.clientSocket.recv(1024)
    return data.decode('utf-8')