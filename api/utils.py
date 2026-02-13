import smtplib
import os
from email.mime.text import MIMEText

def send_alert_email(message: str):

    sender = os.environ.get("EMAIL_USER")
    password = os.environ.get("EMAIL_PASS")
    receiver = os.environ.get("EMAIL_RECEIVER")

    msg = MIMEText(message)
    msg["Subject"] = "KT Exam Alert"
    msg["From"] = sender
    msg["To"] = receiver

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender, password)
        server.send_message(msg)
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print("Email sending failed:", e)
