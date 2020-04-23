import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate
from django.conf import settings

class Email:
    @staticmethod
    def friendRequest(request, to_user_email, to_current_user):
        msg = MIMEMultipart("alternative")
        msg["Subject"] = "New Mate Request"
        msg["From"] = "social@loop.ie"
        msg["Date"] = formatdate(localtime=settings.EMAIL_USE_LOCALTIME)
        msg["To"] = str(to_user_email)
        # Create the plain-text and html version of your message
        html = """<html><body><h1>You have a new mate reuqest</h1>
                            <h2>User {} has sent you a mate request and wants to be mates</h2>
                            <h2>Here is a link to their profile page</h2>
                            <a href='http://127.0.0.1:8000/profiles/detail/{}'>View Profile Page</a>
                            </body></html>""".format(to_current_user,  to_current_user)
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