import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate
from django.conf import settings

class Notification:
    @staticmethod
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
    def sendAdminDeletedPost(request, to_post_maker_email, to_report_reason):
        msg = MIMEMultipart("alternative")
        msg["Subject"] = "Admin Deletes Post"
        msg["From"] = "social@loop.ie"
        msg['Date'] = formatdate(localtime=settings.EMAIL_USE_LOCALTIME)
        msg["To"] = str(to_post_maker_email)
        # Create the plain-text and html version of your message
        html = """<html><body><h1>Admin Deleted Post</h1><h2>An Admin has deleted your post because it had recieved a report with the reason: {}, and the Admin agreed with this decision.</body>
        </html>""".format(to_report_reason)
        # Turn the message into a plain/html MIMETEXT object
        content = MIMEText(html, "html")
        # Add HTML/plain=text parts to MIMEMultipart message
        msg.attach(content)
        #call the method to connect with the server and send email
        Notification.send_email(to_post_maker_email, msg)#

    @staticmethod
    def sendPostLiked(request, to_post_maker_email, to_report_reason):
        msg = MIMEMultipart("alternative")
        msg["Subject"] = "Post Liked"
        msg["From"] = "social@loop.ie"
        msg['Date'] = formatdate(localtime=settings.EMAIL_USE_LOCALTIME)
        msg["To"] = str(to_post_maker_email)
        # Create the plain-text and html version of your message
        html = """<html><body><h1>Your Post Has Been Liked</h1><h2>Your post has been liked by one of your mates. Here is a link to the post: <a href='http://127.0.0.1:8000/'>Your Post</a>.</body>
        </html>"""
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