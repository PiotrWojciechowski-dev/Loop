import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate
from django.conf import settings

class Email:
    @staticmethod
    def messageRecieved(request, to_user_email, to_group_name, to_reciever_username, to_sender_username, to_group_id):
        msg = MIMEMultipart("alternative")
        msg["Subject"] = "New Message from Group"
        msg["From"] = "social@loop.ie"
        msg["Date"] = formatdate(localtime=settings.EMAIL_USE_LOCALTIME)
        msg["To"] = str(to_user_email)
        # Create the plain-text and html version of your message
        html = """<html><body><h1>New Message Recieved</h1>
                            <h2>{} has sent a new message to {}</h2>
                            <h2>Here is a link to the conversation</h2>
                            <a href='http://127.0.0.1:8000/groupchat/{}/{}'>View Message Now</a>
                            </body></html>""".format(to_sender_username, to_group_name, to_group_id, to_group_name)
        # Turn the message into a plain/html MIMETEXT object
        content = MIMEText(html, "html")
        # Add HTML/plain=text parts to MIMEMultipart message
        msg.attach(content)
        #call the method to connect with the server and send email
        Email.send_email(to_user_email, msg)

    @staticmethod
    def addedToGroupChat(request, to_user_email, to_group_name, to_reciever_username, to_sender_username, to_group_owner, to_group_id):
        msg = MIMEMultipart("alternative")
        msg["Subject"] = "Added to new group"
        msg["From"] = "social@loop.ie"
        msg["Date"] = formatdate(localtime=settings.EMAIL_USE_LOCALTIME)
        msg["To"] = str(to_user_email)
        # Create the plain-text and html version of your message
        html = """<html><body><h1>New Message Recieved</h1>
                            <h2>You have been added to a new group {}</h2>
                            <h3>The owner of this group is {}</h3>
                            <h2>Here is a link to the conversation</h2>
                            <a href='http://127.0.0.1:8000/groupchat/{}/{}'>View Message Now</a>
                            </body></html>""".format(to_group_name, to_group_owner, to_group_id, to_group_name)
        # Turn the message into a plain/html MIMETEXT object
        content = MIMEText(html, "html")
        # Add HTML/plain=text parts to MIMEMultipart message
        msg.attach(content)
        #call the method to connect with the server and send email
        Email.send_email(to_user_email, msg)
        
    @staticmethod
    def send_email(request, message):
        port = 25
        smtp_server = "localhost"
        sender_email = "social@loop.ie"
        server = smtplib.SMTP(smtp_server)
        server.sendmail("rrrrrrrrr@hotmail.com", str(request), message.as_string())