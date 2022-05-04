from email import message
import imp
import smtplib
import ssl
from email.message import EmailMessage

subject = "SPAM SPAM SPAM"
body = "jECFTRJ5sqLHeaWW4gegrfFybFJNAMgsem5jzwQBuxTZMzEEk7qQj \
dUs6PLqEskjn3z2F4D2C6t7BmL6matJ3LZ8awW4LJv3yzUgw588P5hCaWaRoDaf2Pg8NoeZbrcX"
sender = "getspammedbot555@gmail.com"
receiver = "getspammedbot555@gmail.com"
password = input("Password: ")
spam_level = int(input("Number of emails: "))

msg = EmailMessage()
msg["From"] = sender
msg["To"] = receiver
msg["Subject"] = subject
msg.set_content(body)


context = ssl.create_default_context()
print("Starting EmailSpam BOT . . .")
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    while spam_level:
        server.login(sender, password)
        server.sendmail(sender, receiver, msg.as_string())
        spam_level -= 1

print("Target spammed successfully.")
