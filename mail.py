import smtplib, ssl

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

user = 'siva.s@masoritherapeutics.com'
password = 'Welcome@123'
smtp = 'smtpout.secureserver.net'

user = 'chatbotnotifier@gmail.com'
password = 'Clever123$'
smtp = 'smtp.gmail.com'

# user = 'info@cleverbrain.in'
# password = 'Clever123$'
# smtp = 'mail.cleverbrain.in'

port = 587

def SendMail(to_address, subject, body):
    sent_from = user
    to_address

    email_text = """\
    Subject: %s
    %s
    """ % (subject, body)
    print(email_text)

    message = MIMEMultipart()
    message['From'] = sent_from
    message['Subject'] = subject
    
    message.attach(MIMEText(body, 'plain'))

    try:
        context = ssl.create_default_context()
        smtp_server = smtplib.SMTP(smtp, port)
        smtp_server.starttls(context=context)
        smtp_server.ehlo()
        smtp_server.login(user, password)
        smtp_server.sendmail(sent_from, to_address, message.as_string())
        smtp_server.close()
        print ("Email sent successfully!")
    except Exception as ex:
        print ("Something went wrong….",ex)



