import socket

host = "localhost"
port = 6767       

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host, port))

fileName = input("Enter the file name: ")
s.send(fileName.encode())

content = s.recv(1024)
print(content.decode())

s.close()
