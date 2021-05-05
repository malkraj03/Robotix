import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 5000))
while True:
    msg = s.recv(1024)
    var = msg.decode("utf-8")
    print(var)
