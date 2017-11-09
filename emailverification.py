import re
import dns.resolver

addressToVerify = raw_input("Email to verify: ")
domainofaddress = addressToVerify.split("@")[1];
match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', addressToVerify)

if match == None:
	print('Bad Syntax')
	raise ValueError('Bad Syntax')

import dns.resolver

records = dns.resolver.query(domainofaddress, 'MX')
mxRecord = records[0].exchange
mxRecord = str(mxRecord)

import socket
import smtplib

# Get local server hostname
host = socket.gethostname()

# SMTP lib setup (use debug level for full output)
server = smtplib.SMTP()
server.set_debuglevel(0)

# SMTP Conversation
server.connect(mxRecord)
server.helo(host)
server.mail('info@makemeafilm.com')
code, message = server.rcpt(str(addressToVerify))
server.quit()

# Assume 250 as Success
if code == 250:
	print('Success')
else:
	print('Bad')
