#Khuram Chughtai

import socket
import sys

if __name__ == "__main__":
	TCP_IP, TCP_PORT = '192.168.1.251', 50650
	size = 1024
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((TCP_IP,int(TCP_PORT)))
	#s.send(command)
	while 1:	
		command = raw_input("Message: ")
		s.send(command)
