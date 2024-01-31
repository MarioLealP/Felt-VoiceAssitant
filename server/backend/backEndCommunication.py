import server.backend.socket as s

def receiveMessage():
    data = s.clientSocket.recv(1024)
    return data.decode('utf-8')

def sendMessage(message):
    message = "S: " + message
    s.clientSocket.send(message.encode('utf-8'))