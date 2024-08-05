import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


def send_email(subject, email, message):
    msg = MIMEMultipart()
    message = message

    password = os.getenv('EMAIL_PASS')
    msg['From'] = os.getenv('EMAIL')
    msg['To'] = email
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com: 587')
    server.starttls()
    server.login(msg['From'], password)
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()
