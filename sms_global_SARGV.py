#!/usr/bin/env python

#=======================================================================#
# script to send messages from feeds or sensors with smsglobal account  #
# By Gabe. github: GaDayas                                        #
# Version 0.2 (sys.argv CLI version), 27 June 2017                      #
#=======================================================================#

import urllib
import sys

#======================================================================#
# script name and 3 arguments in brackets required.                    #
# Example: ./sms_global_SARGV.py "myname" "+61400111222" "Hello World" #
#======================================================================#

if len(sys.argv) != 4:
    print 'ERROR: You must specify sender, recipient and message eg: ./script "sender" "recipient_number" "message"'
    sys.exit(0)

#============================================#
# User / API details in double brackets      #
#============================================#

username = "PUT_API_USERNAME_HERE"
password = "PUT_API_PASSWORD_HERE"

#============================================#
# Sender, recipient & message details        #
#============================================#

sender = sys.argv[1]
recipient = sys.argv[2]
message = sys.argv[3]

#============================================#
# Assemble the URL string here with uname,   #
# password and all message details           #
#============================================#

http_req = "http://www.smsglobal.com/http-api.php?action=sendsms&user="
http_req += urllib.quote(username)
http_req += "&password="
http_req += urllib.quote(password)
http_req += "&from="
http_req += urllib.quote(sender)
http_req += "&to="
http_req += urllib.quote(recipient)
http_req += "&text="
http_req += urllib.quote(message)

# print(http_req) - use this to test / validate URL string

#==============================================================#
# Sending function with details and message to be sent         #
#==============================================================#

def sendText():
	get = urllib.urlopen(http_req)
	req = get.read()
	get.close()
	if req.find("Message accepted for delivery"):
    		print "Message successfully sent"
	else:
    		print "* Message not sent. Check settings and try again *"

sendText()
