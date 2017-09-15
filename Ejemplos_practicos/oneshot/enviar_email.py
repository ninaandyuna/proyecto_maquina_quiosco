#!/usr/bin/python
#-*- coding: utf-8-*-
# Enviar e-mail utilitzado librería smtplib
# 07/09/2017
# -------------------------------------------------------------------

import smtplib
import time
import sys

emisor = 'systemd@system.linux'
receptor = 'adriasototortola@gmail.com'

mensaje = """%s""" %(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
#~ mensaje = """%s""" %(time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()))

try:
	smtpObj = smtplib.SMTP('localhost')
	smtpObj.sendmail(emisor, receptor, mensaje)         
	print "E-mail enviado correctamente"
except smtplib.SMTPException:
	print "Error: imposible enviar el e-mail"

sys.exit(0)
