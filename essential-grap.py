import os
import random
import smtplib, ssl
import string

port = 465  # For SSL
essential_grapx_server = "essential-grapx.gmail.com"
sender_email = "gzamemsatergamer@gmail.com"  # Enter your address
receiver_email = input("Your Email : ")  # Enter receiver address
password = input("Type your password and press enter: ")
message = f"""
{random.radient(1000, 9999)}
"""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(essential_grapx_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
