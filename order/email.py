import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate
from django.conf import settings

class Email:
    @staticmethod
    def sendOrderConfirmation(request, to_user_email, to_order_id, to_addressline1, to_addressline2, to_code, to_city, to_county, to_country, to_total):
        msg = MIMEMultipart("alternative")
        msg["Subject"] = "Order Confirmation Email"
        msg["From"] = "sales@loop.ie"
        msg['Date'] = formatdate(localtime=settings.EMAIL_USE_LOCALTIME)
        msg["To"] = str(to_user_email)
        # Create the plain-text and html version of your message
        html = """<html><body><h1>Order Confirmation</h1><h2>Your order number is {}.
        Please pay for your order before we ship. Amount to pay is €{}. There is a link here for payment, shipping will happen after payment</h2><a href='http://127.0.0.1:8000/order/payment/{}'>Pay Now</a><h3>Address:</h3><h3>   {}</h3><h3>   {}</h3><h3>   {}</h3>
        <h3>   {}</h3><h3>   {}</h3><h3>   {}</h3></body>
        </html>""".format(to_order_id, to_total, to_order_id, to_addressline1, to_addressline2, to_code, to_city, to_county, to_country)
        # Turn the message into a plain/html MIMETEXT object
        content = MIMEText(html, "html")
        # Add HTML/plain=text parts to MIMEMultipart message
        msg.attach(content)
        #call the method to connect with the server and send email
        Email.send_email(to_user_email, msg)

    @staticmethod
    def sendPaymentConfirmation(request, to_user_email, to_order_id, to_addressline1, to_addressline2, to_code, to_city, to_county, to_country, to_total):
        msg = MIMEMultipart("alternative")
        msg["Subject"] = "Payment Confirmation Email"
        msg["From"] = "sales@loop.ie"
        msg['Date'] = formatdate(localtime=settings.EMAIL_USE_LOCALTIME)
        msg["To"] = str(to_user_email)
        # Create the plain-text and html version of your message
        html = """<html><body><h1>Payment Confirmation</h1><h2>Your order number is {}.
        Thank you for paying for your order we will ship in 3-5 busuness days. You paid €{}</h2><h3>Address:</h3><h3>   {}</h3><h3>   {}</h3><h3>   {}</h3>
        <h3>   {}</h3><h3>   {}</h3><h3>   {}</h3></body>
        </html>""".format(to_order_id, to_total, to_addressline1, to_addressline2, to_code, to_city, to_county, to_country)
        # Turn the message into a plain/html MIMETEXT object
        content = MIMEText(html, "html")
        # Add HTML/plain=text parts to MIMEMultipart message
        msg.attach(content)
        #call the method to connect with the server and send email
        Email.send_email(to_user_email, msg)

    @staticmethod
    def sendCancelationConfirmation(request, to_user_email, to_order_id, to_addressline1, to_addressline2, to_code, to_city, to_county, to_country):
        msg = MIMEMultipart("alternative")
        msg["Subject"] = "Order Cancelation Confirmation Email"
        msg["From"] = "sales@loop.ie"
        msg['Date'] = formatdate(localtime=settings.EMAIL_USE_LOCALTIME)
        msg["To"] = str(to_user_email)
        # Create the plain-text and html version of your message
        html = """<html><body><h1>Order Cancelation</h1><h2>Your order number is {}.
        Your Order has now been cancelled.</h2><h3>Address:</h3><h3>   {}</h3><h3>   {}</h3><h3>   {}</h3>
        <h3>   {}</h3><h3>   {}</h3><h3>   {}</h3></body>
        </html>""".format(to_order_id, to_addressline1, to_addressline2, to_code, to_city, to_county, to_country)
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
        sender_email = "sales@loop.ie"
        server = smtplib.SMTP(smtp_server)
        server.sendmail("rrrrrrrrr@hotmail.com", str(request), message.as_string())