#!/usr/bin/python2
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
'''
socket --- ip(4Byte)+port(2bytes) -- 6bytes
'''




'''s.sendto(n1,("127.0.0.1",7777))
s.sendto(n2,("127.0.0.1",7777))'''



for i in range(100000):
	     msg=raw_input("enter your msg :  ")
             s.sendto(msg,("127.0.0.1",7777))
	     print s.recvfrom(1000)




