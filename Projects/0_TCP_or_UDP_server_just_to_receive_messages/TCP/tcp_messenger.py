import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
message = b"H3ll0, W0rld!"

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #create the socket
sock.connect((TCP_IP, TCP_PORT)) #connect to the server
sock.send(message)
data = sock.recv(1024)
sock.close()

print("Received data:", data) #print message from server