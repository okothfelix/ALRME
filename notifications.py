import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate


def email_notification_section(send_to,  message):
    msg = MIMEMultipart()
    msg['From'] = 'accounts@domain.com'
    msg['To'] = send_to
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = "CLIENT ENQUIRY"
    msg.attach(MIMEText(message))
    smtp = smtplib.SMTP_SSL('mail.domain.com', 465)
    smtp.ehlo()
    smtp.login('accounts@domain.com', 'account_password')
    smtp.sendmail('accounts@domain.com', send_to, msg.as_string())
    smtp.quit()
