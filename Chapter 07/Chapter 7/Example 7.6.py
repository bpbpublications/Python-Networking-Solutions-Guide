import smtplib
from email import message
import mimetypes
from netmiko import Netmiko

def collect_configuration():
    host = ["10.10.10.1", "10.10.10.2", "10.10.10.3"]
    for ip in host:
        device = { "host": ip, "username": "admin", "password": "cisco", "device_type": "cisco_ios"}
        net_connect = Netmiko(**device)
        output = net_connect.send_command("show run")
        with open (f"{ip} config.txt","w") as wr:
            wr.write(output)
        net_connect.disconnect()
    return host

host = collect_configuration()

mail_from = "example@gmail.com"
mail_password = "16-DIGIT-PASSWORD"
mail_to = "example@gmail.com"
mail_subject = "Router Configurations"
mail_content = "Hi,\nYou can find the all configuration files in the attachment."

send = message.EmailMessage()
send.add_header("From", mail_from)
send.add_header("To", mail_to)
send.add_header("Subject", mail_subject)
send.set_content(mail_content)

for file in host:
    filename = f"{file} config.txt"
    with open(filename, "rb") as r:
        attached_file = r.read()

    mime_type, encoding = mimetypes.guess_type(filename)
    send.add_attachment(attached_file, maintype=mime_type.split("/")[0],
                        subtype=mime_type.split("/")[1], filename=filename)

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(mail_from, mail_password)
    smtp.sendmail(mail_from, mail_to, send.as_string())
