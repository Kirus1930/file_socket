import socket
s = socket.socket()
host = input("enter host address of sender: ")
port = 8080
s.connect((host, port))
print("connected")
filename = input("enter incoming filename: ")
file = open(filename, "wb")
while True:
    file_data = s.recv(4096)
    file.write(file_data)
    if not file_data:
        break
file.close()
print("file downloaded")
