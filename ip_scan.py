#!/bin/env python

import socket
import sys

ip_prefix = '192.168.199.'
ip_suffix = 0

while ip_suffix < 256:
	ip = ip_prefix + str(ip_suffix)
	print 'ip = ' + ip
	try:
		client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		client.settimeout(1)
		client.connect((ip, 22))
		client_file = client.makefile('w', 1024)
		greetings = client_file.readline().strip()
		print greetings
		if greetings.find('SSH') != -1:
			break
	except StandardError, e:
		print 'Error: ', e
	finally:
		ip_suffix = ip_suffix + 1
#sys.stdout.flush()
