from netmiko import Netmiko
import smtplib
from email import message
import mimetypes

def collect_configuration():
    host = ["192.168.163.135", "192.168.163.136", "192.168.163.137"]
    for ip in host:
        device = {"host": ip, "username": "ubuntu", "password": "ubuntu", "device_type": "linux"}
        command = "cat /var/log/syslog | grep 'SSH\|ssh'"
        net_connect = Netmiko(**device)
        output = net_connect.send_command(command)
        net_connect.disconnect()
        with open (f"{ip} syslog.txt","a") as w:
            w.write(output)
    return host

host = collect_configuration()

mail_from = "example@gmail.com"
mail_password = "16-DIGIT-CODE"
mail_to = "example@gmail.com"
mail_subject = "Router Configurations"
mail_content = "Hi,\nYou can find the all configuration files in the attachment."

send = message.EmailMessage()
send.add_header("From", mail_from)
send.add_header("To", mail_to)
send.add_header("Subject", mail_subject)
send.set_content(mail_content)

for file in host:
    filename = f"{file} syslog.txt"
    with open(filename, "rb") as r:
        attached_file = r.read()

    mime_type, encoding = mimetypes.guess_type(filename)
    send.add_attachment(attached_file, maintype=mime_type.split("/")[0],
                        subtype=mime_type.split("/")[1], filename=filename)

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(mail_from, mail_password)
    smtp.sendmail(mail_from, mail_to, send.as_string())
