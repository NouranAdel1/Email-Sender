import smtplib

from email import encoders
from email import message
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP("smtp-mail.outlook.com", port=587)
server.starttls()

sender = "goodmorningnouran@outlook.com"
recipient = "nouranadel888@gmail.com"

server.login(sender, "Nouran555")
print("login success")


msg = MIMEMultipart()
msg['From']= 'goodmorningnouran@outlook.com'
msg['To']= 'Nouranadel888@gmail.com'
msg['Subject']= 'TEST'


with open('test.txt','r') as f:
    test = f.read()

msg.attach(MIMEText(test, 'plain'))
filename = 'cat.jpg'
attachment = open(filename, 'rb')

p = MIMEBase('application','octet-stream')
p.set_payload(attachment.read())


encoders.encode_base64(p)
p.add_header('Content-Disposition',f'attachement; filename={filename}')
msg.attach(p)

text = msg.as_string()
server.sendmail('goodmorningnouran@outlook.com', 'Nouranadel888@gmail.com', text)
print("mail has been sent")
