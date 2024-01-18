import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
Message = b"H3ll0 W0rld!"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(Message, (UDP_IP,UDP_PORT))