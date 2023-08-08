from email.message import EmailMessage
from senha import password
import ssl
import smtplib

email_sender = "juanfernandodemourasilva@gmail.com"
email_password = password

email_receiver = 'lreleun697@tempmailfree.com'

assunto = 'Test email'
corpo = '''
  Se chegou aqui funciona
'''

Email = EmailMessage()
Email['from'] = email_sender
Email['to'] = email_receiver
Email['subject'] = assunto
Email.set_content(corpo)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, Email.as_string())
