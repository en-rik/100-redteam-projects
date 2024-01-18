import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
message = b"Hello messenger"

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #create the socket
sock.bind((TCP_IP, TCP_PORT)) #bind the address
sock.listen(1) 

conn, addr = sock.accept()  
print('Connection adderss:', addr)

while 1:
    data = conn.recv(24) #buffer 
    if not data:break
    print("Message:", data )
    conn.send(message)  #send message back to the messenger
conn.close()