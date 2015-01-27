#encoding:utf-8
import socket

HOST = ''
PORT = 50007
BUFSIZE = 1024

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(1) #最大连接数
while True:
	conn,addr = s.accept() #return value is a pair (conn, address)
	print 'Connected by:',addr
	while True:
		data = conn.recv(BUFSIZE)
		if not data:
			break
		conn.send(data)
conn.close()
