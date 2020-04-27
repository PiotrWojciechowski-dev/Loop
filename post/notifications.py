import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate
from django.conf import settings

class Notification:
    @staticmethod
    #sending emails to your mates list informing them you made a post
    def sendMatesPostConfirmation(request, to_mate_email, your_mate):
        msg = MIMEMultipart("alternative")
        msg["Subject"] = "Mate Post Upload"
        msg["From"] = "social@loop.ie"
        msg['Date'] = formatdate(localtime=settings.EMAIL_USE_LOCALTIME)
        msg["To"] = str(to_mate_email)
        # Create the plain-text and html version of your message
        html = """<html><body><h1>Mate Post Upload</h1><h2>Your mate {} has made a post. Here is a link to the post: <a href='http://127.0.0.1:8000/'>Mates Post</a>.</body>
        </html>""".format(your_mate)
        # Turn the message into a plain/html MIMETEXT object
        content = MIMEText(html, "html")
        # Add HTML/plain=text parts to MIMEMultipart message
        msg.attach(content)
        #call the method to connect with the server and send email
        Notification.send_email(to_mate_email, msg)

    @staticmethod
    #sending email to post owner informing them you made a comment on thier post
    def sendMatesCommentConfirmation(request, to_post_maker_email, your_mate):
        msg = MIMEMultipart("alternative")
        msg["Subject"] = "Mate Comment Upload"
        msg["From"] = "social@loop.ie"
        msg['Date'] = formatdate(localtime=settings.EMAIL_USE_LOCALTIME)
        msg["To"] = str(to_post_maker_email)
        # Create the plain-text and html version of your message
        html = """<html><body><h1>Mate Comment Upload</h1><h2>{} has made a comment on your post. Here is a link to the post: <a href='http://127.0.0.1:8000/'>Mates Comment</a>.</body>
        </html>""".format(your_mate)
        # Turn the message into a plain/html MIMETEXT object
        content = MIMEText(html, "html")
        # Add HTML/plain=text parts to MIMEMultipart message
        msg.attach(content)
        #call the method to connect with the server and send email
        Notification.send_email(to_post_maker_email, msg)
    

    
    @staticmethod
    def send_email(request, message):
        port = 25
        smtp_server = "localhost"
        sender_email = "sales@loop.ie"
        server = smtplib.SMTP(smtp_server)
        server.sendmail("rrrrrrrrr@hotmail.com", str(request), message.as_string())