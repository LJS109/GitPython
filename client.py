#encoding:utf-8
import socket

HOST = 'localhost'
PORT = 50007
BUFSIZE = 1024
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))
s.send('Hello World')
data = s.recv(BUFSIZE)
s.close()
print 'Received:',repr(data)
