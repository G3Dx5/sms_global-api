#!/usr/bin/env python

#=======================================================================#
# script to send messages from feeds or sensors with smsglobal account  #
# By Gabe. github: GaDayas                                        #
# Version 0.1 (basic), 27 June 2017                                     #
# Runs with sender, recipient and message hardcoded in the script       #
# Example: ./sms_global_HCO.py                                          #
#=======================================================================#

import urllib

#===========================================#
# User / API details in brackets            #
#===========================================#

username = "API_USERNAME"
password = "API_PASSWORD"

#=======================================#
# Sender, recipient & message details   #
#=======================================#

sender = "SENDER_NAAME_YOU SELECT"
recipient = "RECIPIENT_MOBILE"
message = "Hello World!"

#=====================================================================#
# Assemble the URL string here uname, password and message details    #
#=====================================================================#

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
