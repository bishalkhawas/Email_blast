import csv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from secret import email, pwd 

email_sender = email 
email_password = pwd 
subject = ""


with open('hackathon.csv','r') as csv_file:
	csv_reader = csv.reader(csv_file)
	for line in csv_reader:
		text=("Dear " +line[1]+","+"\n"
		 "")
		# print(text)

		send_email = line[0]
		msg = MIMEMultipart()
		msg['From'] = email_sender
		msg['To'] = send_email
		msg['Subject'] = subject
		msg.attach(MIMEText(text,"plain"))
		text = msg.as_string()

		server = smtplib.SMTP_SSL("smtp.gmail.com",465)
		server.login(email_sender,email_password)
		server.sendmail(email_sender,send_email,text)

		server.quit()
