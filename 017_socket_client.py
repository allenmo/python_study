#!/usr/bin/python3

#Socket client example in python

import socket
import sys

# host = 'www.pythonprogramminglanguage.com'
host = 'www.allstack.net'
port = 7000 # web

# create socket
print('# Creating Socket')
try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
	print('Failed to create socket')
	sys.exit()

print('# Getting remote IP address')
try:
	remote_ip = socket.gethostbyname( host)
except socket.gaierror:
	print('Hostname could not be resolved. Exiting')
	sys.exit()

# Connect to remote server
remote_ip = "127.0.0.1"
print('# Connectiong to server, ' + host + ' (' + remote_ip + ')')
s.connect((remote_ip, port))

#Send data to remote server
print('# Sending data to server')
#irequest = b"GET / HTTP/1.0\r\n\r\n"
request = "GET / HTTP/1.0\r\n\r\n"


try:
	s.sendall(request.encode())
	#s.sendall(request)
except socket.error:
	print('Send failed')
	sys.exit()

#Receive data
print('# Receive data from server')
reply = s.recv(1024).decode()

print(reply)

