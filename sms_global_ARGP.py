#!/usr/bin/env python

#=======================================================================#
# script to send messages from feeds or sensors with smsglobal account  #
# github: G3Dx5                                                         #
# Version 0.3 (argparse CLI version), 27 June 2017                      #
#=======================================================================#

import urllib
import argparse
import logging 

#==================================================================#
# Using the argparse module for options.                           #
# Example ./sms_global_ARGP.py -s me -r +61400111222 -m "Hi there" #
#==================================================================#

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--sender", help="name of sender")
parser.add_argument("-r", "--recipient", help="phone number of recipient")
parser.add_argument("-m", "--message", help="message to be sent")
args = parser.parse_args()

#===============================================#
# User / API details                            #
#===============================================#

username = "PUT_API_USERNAAME_HERE"
password = "PUT_API_PASSWORD_HERE"

#===============================================#
# Sender, recipient & message details           #
#===============================================#

sender = args.sender
recipient = args.recipient
message =  args.message

#===============================================#
# Assemble the URL string here with uname,      #
# password and all message details              #
#===============================================#

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

#===============================================#
# Sending function with details and message     #
# to be sent                                    #
#===============================================#

logging.basicConfig(filename='smstraffic.log', level=logging.DEBUG,
    format='%(asctime)s:%(levelname)s:%(message)s')

def sendText():
	get = urllib.urlopen(http_req)
	req = get.read()
	get.close()
	if req.find("Message accepted for delivery"):
		print("Message successfully sent")
		logging.info("message sent successfully")
	else:
		print("* Message not sent. Check settings and try again *")
		logging.info("message failed")

sendText()
