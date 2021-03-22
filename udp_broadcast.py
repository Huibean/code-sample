import socket
import time
udpServer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
udpServer.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
udpServer.settimeout(0.2)

msg = b'from raspberry pi'
while True:
    udpServer.sendto(msg, ('<broadcast>', 5005))
    time.sleep(1)
