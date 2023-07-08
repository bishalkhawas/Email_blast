import csv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from secret import email, pwd 

email_sender = email 
email_password = pwd 
subject = "Hello Greeting From Tech Medhavi"


with open('hackathon.csv','r') as csv_file:
	csv_reader = csv.reader(csv_file)
	for line in csv_reader:
		text=("Dear " +line[1]+","+"\n"
	"As we mentions before, participate team should submit their project by saturday 6:00 pm."+"\n"
	"Please Submit your Project before 6 pm of Saturday." +"\n"
	"Participate team who submit their project after 6 pm will not accepted. "+"\n"+"\n"
	"After the submission of their project participate have to prepare documentation."+"\n"
	"Here is the link for references of documentation. "+"\n"
	"https://ec.europa.eu/research/participants/documents/downloadPublic?documentIds=080166e5d1408d63&appId=PPGMS."+"\n"+" \n"
	"Here are a few important details to keep in mind "+"\n"+"\n"
	"https://docs.google.com/document/d/1Fn78aYOBqoEO02Icmem8sIj_6wZLxWrq6Cyl6LAKl5w"+"\n"+"\n"
		"If you have any questions or require further information, please do not hesitate to reach out to us "+"\n"
		"at 9860449052. We are here to assist you throughout this journey."+"\n"+"\n"
		"Best regards, "+"\n"+"\n"
		"MedhaviCodeQuest, "+"\n"+"\n"
		 " Tech Medhavi")
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