# sms_global-api

**Python code to allow users with an smsglobal account to programmatically send information by SMS.** 

The repository contains three variations on the code: 

- sms_global_HCO.py - A 'hard coded' version that contains the sender name (whatever you supply), recipient phone number and the message already in the script.  This is useful where it wil be an automated  message that is triggered withoout user interaction, for example an event on a local machine where the reipient will always be the same. If successful will return "Message successfully sent".  If there is a problem, will return "Message not sent. Check settings and try again".

Example: ./sms_global_HCO.py   

- ****sms_global_ARGP.py - A variation on the code that uses the python argparse module to obtain mmessage settings where -s is the sender (whatever you supply), -r is the recipient phone number and -m is the message in quottion marks. If successful will return "Message successfully sent".  If there is a problem, will return "Message not sent. Check settings and try again".
    
Example: ./sms_global_ARGP.py -s me -r +61400111222 -m "Hi there"


Released under MIT License, 2017
