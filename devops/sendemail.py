# script for send email notification #

import pandas as pd
import smtplib

from_addr = "eugene.kuznetsou@gmail.com"
password = "ozzvywxcwrxhtzlg". # app password from Gmail
to_addr = "eugene.kuznetsou@gmail.com"

e = pd.read_excel("1.xlsx") # list of emails
emails = e['Emails'].values

server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(from_addr, password)

msg = "Email from script"
subj = "ALARM"

body = "subject: {}\n\n{}".format(subj,msg)

for emial in emails:
	server.sendmail(from_addr, emails, body)

server.quit()