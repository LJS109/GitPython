#encoding:utf-8
import socket
import time
HOST = 'localhost'
PORT = 50007
BUFSIZE = 1024
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))
while True:
	s.send('Hello World %s' % time.ctime())
	data = s.recv(BUFSIZE)
	if not data:
		print 'Received:',repr(data)
s.close()
