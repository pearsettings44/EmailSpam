from email import message
import imp
import smtplib
import ssl
from email.message import EmailMessage

subject = "SPAM SPAM SPAM"
sender = "getspammedbot555@gmail.com"
receiver = "getspammedbot555@gmail.com"
password = input("Password: ")
spam_level = int(input("Number of emails: "))

with open("spam.txt") as file:
    body = file.read()

msg = EmailMessage()
msg["From"] = sender
msg["To"] = receiver
msg["Subject"] = subject
msg.set_content(body)

context = ssl.create_default_context()

print("Starting EmailSpam BOT . . .")
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    total = 0
    while total != spam_level:
        server.login(sender, password)
        server.sendmail(sender, receiver, msg.as_string())
        total += 1
        print(f"Sending spam email {total}/{spam_level}")

print("Target spammed successfully.")
