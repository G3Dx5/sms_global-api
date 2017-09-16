# sms_global-api

Python code to allow users with an smsglobal account to programmatically send information by SMS. 

The repository contains three variations on the code: 

sms_global_HCO.py - A 'hard coded' version that contains the sender name (whatever you supply), recipient phone number and the message already in the script.  This is useful where it wil be an automated  message that is triggered withoout user interaction, for example an event on a local machine where the reipient will always be the same. If successful the will return "Message successfully sent".  If there is a problem, will return "Message not sent. Check settings and try again".

Example : ./sms_global_HCO.py   


