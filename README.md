# sms_global-api

## Python code to allow users with an smsglobal account to programmatically send information by SMS.

Code Variations: 

The repository contains three variations on the code / functionality: 

- sms_global_HCO.py - A 'hard coded' version that contains the sender name (whatever you supply), recipient phone number and the message already in the script.  This is useful where it wil be an automated  message that is triggered withoout user interaction, for example an event on a local machine where the reipient will always be the same. If successful will return "Message successfully sent".  If there is a problem, will return "Message not sent. Check settings and try again".

    Example Usage: ./sms_global_HCO.py   

- sms_global_ARGP.py - A variation on the code that uses the python argparse module to obtain message settings where -s is the sender name (whatever you supply), -r is the recipient phone number and -m is the message in quotation marks. If successful will return "Message successfully sent".  If there is a problem, will return "Message not sent. Check settings and try again".
    
    Example Usage: ./sms_global_ARGP.py -s me -r +61400111222 -m "Hi there"

- sms_global_SARGV.py - a variation on the code that uses the python sys.argv function to obtain message settings where -s is the sender name (whatever you supply), -r is the recipient phone number and -m is the message. Requires all fields (except the script of course!) in quotation marks. If successful will return "Message successfully sent".  If there is a problem, will return "Message not sent. Check settings and try again".

    Example Usage: ./sms_global_SARGV.py "myname" "+61400111222" "Hello World"

**Licence:**

Released under MIT License

GaDayas 2017
