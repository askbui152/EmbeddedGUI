# #Khuram Chughtai

import socket
import sys


if __name__ == "__main__":
	TCP_IP, TCP_PORT = '192.168.10.107', 2000
	size = 1024
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((TCP_IP,int(TCP_PORT)))
	command = b'R'
	#s.send(command)
	while 1:	
		#command = input("Message: ")
		s.send(command)
		
# import sys
# import socket
# import time

# host = ''
# port = 50000
# backlog = 5
# size = 1024

# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.bind((host,port))
# s.listen(1)

# while True:
	# print >> sys.stderr, 'waiting for a connection'
	# connection, client_address = s.accept()
	
	# #try:
	# print >>sys.stderr, 'connection from', client_address
		
		# #while True:
# #s.close()

