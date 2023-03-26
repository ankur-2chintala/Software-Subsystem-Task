import socket

serverIP = "172.17.29.11"
serverPORT = 6000

serverADDRESS = (serverIP, serverPORT)
bufferSize = 1024

UDPClientSocket = socket.socket(family = socket.AF_INET, type = socket.SOCK_DGRAM)

message = "Hi, my name is Ankur Renduchintala. My ID no is 2021B5A71159P"

bytestosend = str.encode(message)

x = 0
while(x < 10):
    UDPClientSocket.sendto(bytestosend, serverADDRESS)
    x += 1
print(message)
