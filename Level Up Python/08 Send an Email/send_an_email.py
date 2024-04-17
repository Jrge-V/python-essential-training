# Sending email using smtp library
# Steps > Google account with 2FA enabled,
# go to `myaccount.google.com/apppasswords` and create an App and copy the code in a .env
import smtplib

import os
# pip install python-dotenv
from dotenv import load_dotenv


def send_email(sender_handle, sender_subject, sender_message):
    # for this program I'll make the sender_handle and receiver_handle be the same
    receiver_handle = sender_handle

    text = f'Subject: {sender_subject}\n{sender_message}'

    # start smtp server
    # default values for host and port, can also use 'smtp.office365.com' if I want to do it via outlook
    # open with a context manager 'with' to automatically close the connection when done
    with smtplib.SMTP('smtp.gmail.com', 587) as server:

        server.starttls()

        # load env key
        load_dotenv()
        app_password = os.getenv('KEY')
        # log in to the server using the sender handle and password from app password in my .env file
        server.login(sender_handle, app_password)

        # send the email
        server.sendmail(sender_handle, receiver_handle, text)


# Test code
send_email('jorgeg.verduzcoespinoza@gmail.com', 'Notification', 'Everything is awesome!')
