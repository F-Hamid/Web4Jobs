import socket

serverSocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)


host=socket.gethostbyname()
port= 444

serverSocket.bind((host, port))
serverSocket.listen(5)


while True:
    clientsocket, adress= serverSocket.accept()
    print (f"received connection from {adress} ")
    

    massage="Hello from the srver, Thank you for you connection"
    clientsocket.send(message)


    clientsocket.close()
