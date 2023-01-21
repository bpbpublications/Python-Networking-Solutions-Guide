    def send_logs_by_email():
        with open("input/device_list.txt") as r:
            device_list = r.read().splitlines()
        with open("input/command_list.txt") as r:
            command_list = r.read().splitlines()

        def concurrent(ip):
            print(f"---Try to Login:{ip}---")
            device = {"host": ip, "username": "admin", "password": "cisco", "device_type": "cisco_ios"}
            net_connect = Netmiko(**device)
            hostname = net_connect.find_prompt()
            for command in command_list:
                output = net_connect.send_command(command, strip_command=False)
                with open(f"output/{ip} logs.txt", "a") as w:
                    w.write(f"{hostname} {output}\n\n")

        with ThreadPoolExecutor(max_workers=25) as executor:
            executor.map(concurrent, device_list)

        print("\nSending Email")
        mail_from = "example@gmail.com"
        mail_password = "16-DIGIT-PASSWORD"
        mail_to = "example@gmail.com"
        mail_subject = "Device Logs"
        mail_content = "Hi,\nYou can find the all device log files in the attachment."

        send = message.EmailMessage()
        send.add_header("From", mail_from)
        send.add_header("To", mail_to)
        send.add_header("Subject", mail_subject)
        send.set_content(mail_content)

        for file in device_list:
            filename = f"output/{file} logs.txt"
            with open(filename, "rb") as r:
                attached_file = r.read()

            mime_type, encoding = mimetypes.guess_type(filename)
            send.add_attachment(attached_file, maintype=mime_type.split("/")[0],
                                subtype=mime_type.split("/")[1], filename=filename)

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(mail_from, mail_password)
            smtp.sendmail(mail_from, mail_to, send.as_string())
