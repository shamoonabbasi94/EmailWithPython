'''
CREATE GMAIL ACCOUNT, SET TWO FACTOR AUTHENTICATIO, EDIT URL hit https://myaccount.google.com/apppasswords, THEN
SET A CUSTOM APP AND COPY AUTO GENERATED 16 DIGIT CODE AND SET IN PASSWORD FIELD IN YOUR CODE. 
'''


import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = 'sender address'
receiver_email = 'recepient address'

password='your 16 digit code'
subject = 'Account Created'
message = 'Python Script is working Fine'

msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject
msg.attach(MIMEText(message, 'plain'))


with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
    server.login(sender_email, password)  
    server.sendmail(sender_email, receiver_email, msg.as_string())  
    print('Email sent successfully!')
