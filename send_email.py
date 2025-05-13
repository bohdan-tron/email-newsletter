import smtplib, ssl
import os

  
def send_email(message):
  port = 465
  smtp_server = os.environ.get('SMTP_SERVER', 'smtp.gmail.com')
  sender_email = os.environ.get('SENDER_EMAIL')
  receiver_email = os.environ.get('RECEIVER_EMAIL', 'Return.ginger@gmail.com')
  password = os.environ.get('EMAIL_PASSWORD')
  context = ssl.create_default_context()
  
  with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
# def send_email(message):
#     host = "smtp.gmail.com"
#     port = 465

#     username = "app8flask@gmail.com"
#     password = "pmuuyjaxfejfpxkc"

#     receiver = "app8flask@gmail.com"
#     context = ssl.create_default_context()

#     with smtplib.SMTP_SSL(host, port, context=context) as server:
#         server.login(username, password)
#         server.sendmail(username, receiver, message)