import smtplib
import random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

mails = ["pujithavarre14@gmail.com","sowjijettiboina@gmail.com","harinich966@gmail.com"]

for i in mails:
    otp = random.randint(1111,9999)
    body = f"OTP for Verification is {otp}"

    msg = MIMEMultipart()
    msg["From"] = "pujithavarre14@gmail.com"
    msg["To"] = i
    msg["Subject"] = "OTP For Validation"
    msg.attach(MIMEText(body,'plain'))

    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login("pujithavarre14@gmail.com","vjab bmne xjxu ptvz")
    server.send_message(msg)
    server.quit()

    cotp = int(input("Enter OTP Recieved: "))

    if otp == cotp:
        print("OTP Verification Success")
    else:
        print("Invalid OTP")







 
