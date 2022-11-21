import socket

host = input("Nom de la machine: ")
port = int(input("Numéro du port connecté: "))
message = input("Message pour le serveur:")

client_socket = socket.socket()
client_socket.connect((host, port))
client_socket.send(message.encode())
data = client_socket.recv(1024).decode()

while data != "exit" and data != "bye":
    client_socket.send(message.encode())
    data = client_socket.recv(1024).decode()

client_socket.close()
