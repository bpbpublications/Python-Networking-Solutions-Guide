import smtplib
from email import message

mail_from = "example@gmail.com"       #The value must be Gmail address
mail_password = "16-DIGIT-PASSWORD"
mail_to = "example@gmail.com"
mail_to_cc = "example@gmail.com"
mail_to_bcc = "example@gmail.com"
mail_subject = "Test Email"
mail_content = "Hi,\nThis is a test email"

send = message.EmailMessage()
send.add_header("From", mail_from)
send.add_header("To", mail_to)
send.add_header("Cc", mail_to_cc)
send.add_header("Bcc", mail_to_bcc)
send.add_header("Subject", mail_subject)
send.set_content(mail_content)

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(mail_from, mail_password)
    smtp.sendmail(mail_from, mail_to, send.as_string())
