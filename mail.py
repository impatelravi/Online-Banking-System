#!C:\Python\Python27\python.exe -u

import smtplib

message = """From: From Person <from@fromdomain.com>
To: To Person <to@todomain.com>
MIME-Version: 1.0
Content-type: text/html
Subject: SMTP HTML e-mail test

This is an e-mail message to be sent in HTML format

<b>This is HTML message.</b>
<h1>This is headline.</h1>
"""

try:
   smtpObj = smtplib.SMTP('mail.impatelravi@gmail.com', 25)
   smtpObj.sendmail(impatelravi@gmail.com, impatelravi@gmail.com, message)         
   print "Successfully sent email"
except SMTPException:
   print "Error: unable to send email"