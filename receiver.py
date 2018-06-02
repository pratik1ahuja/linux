#!/usr/bin/python2
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.bind(("127.0.0.1",7777))

for i in hy hello:
	data = s.recvfrom(10000)
	print data
	s.sendto("hello",data[1])
	
	
