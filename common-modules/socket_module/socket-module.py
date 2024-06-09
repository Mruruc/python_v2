import socket

socket_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket_socket.connect(("data.pr4e.org", 80))
socket_socket.send('GET http://data.pr4e.org/romeo.txt HTTP/1.0 \n\n'.encode())

file_handler = open("test.html", "a")

while True:
    data = socket_socket.recv(512)
    if len(data) < 1:
        break
    file_handler.write(data.decode())


file_handler.close()
socket_socket.close()
