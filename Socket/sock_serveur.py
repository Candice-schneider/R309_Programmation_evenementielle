import socket
host = input("Nom de la machine: ")
port = int(input("Numéro du port connecté: "))
reply = input("réponse pour le client:")

server_socket = socket.socket()
server_socket.bind((host, port))
server_socket.listen(1)
conn, address = server_socket.accept()
data = conn.recv(1024).decode()

while data != "exit" and data != "bye":
    data = conn.recv(1024).decode()
    print(data)
    conn.send(reply.encode())

conn.close()

