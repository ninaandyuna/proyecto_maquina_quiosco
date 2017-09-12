#!/usr/bin/python
#-*- coding: utf-8-*-
# ----------------------------------------------------------------------

import os,sys,socket
from subprocess import Popen,PIPE

HOST = ''
PORT = 50012

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

sys.stderr.write("%s\n" %(os.getpid()))

while True:
	conn, addr = s.accept()
	sys.stderr.write("Connected by %s\n" %(addr[0]))
	command = "/usr/bin/date"
	pipeData = Popen(command,shell=True,stdout=PIPE,stderr=PIPE)
	for line in pipeData.stdout:
		conn.sendall(line)
	conn.close()

sys.exit(0)
