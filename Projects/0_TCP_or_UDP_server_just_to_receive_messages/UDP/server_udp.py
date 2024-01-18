import socket 

UDP_IP = "127.0.0.1" 
UDP_PORT = 5005      


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  #create the socket
sock.bind((UDP_IP, UDP_PORT))  #bind the ip and the port

message = 0   #counter for the messages
while message < 1: #accept only one message
    data, addr = sock.recvfrom(1024) #buffer
    print("Message: %s" % data)
    message=message+1