from multiprocessing.connection import wait
import smtplib
import ssl
from email.message import EmailMessage
import random

#Email subject
subject = "SPAM SPAM SPAM"
#Email sender
sender = "getspammedbot555@gmail.com"
#Email of target
target = input("target email: ")
#Password of sender
password = input("Sender password: ")
#Number of emails sent to target
spam_level = int(input("Number of emails: "))

#Email Message Details
msg = EmailMessage()
msg["From"] = sender
msg["To"] = target
msg["Subject"] = subject

#Collection of all spam copypastas
bodys = []
for i in range(1, 10):
    with open(f"./spam_msgs/spam{i}.txt") as file:
        body = file.read()
        bodys.append(body)


#Sending the emails
print("Starting EmailSpam BOT . . .")
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender, password)
    total = 0
    while total != spam_level:
        #Get random spam msg
        msg.set_content(bodys[random.randint(0, len(bodys) - 1)])
        server.sendmail(sender, target, msg.as_string())
        total += 1
        print(f"Sending spam email {total}/{spam_level}")

print("Target spammed successfully.")
