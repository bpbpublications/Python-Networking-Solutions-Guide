from netmiko import Netmiko
from concurrent.futures import ThreadPoolExecutor
from re import findall, split
from pandas import DataFrame
import smtplib
from email import message
import mimetypes
from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_netmiko import netmiko_send_config, netmiko_file_transfer
from paramiko import SSHClient, AutoAddPolicy

class collect_logs:
    def from_one_device(ip, username, password,command):
        device = { "host": ip, "username": username, "password": password, "device_type": "cisco_ios"}
        net_connect = Netmiko(**device)
        show_output = net_connect.send_command(command)
        print(show_output)


################################################################################################


    def from_multiple_devices():
        with open("input/device_list.txt") as r:
            device_list = r.read().splitlines()
        with open("input/command_list.txt") as r:
            command_list = r.read().splitlines()

        def concurrent(ip):
                device = {"host": ip, "username": "admin", "password": "cisco", "device_type": "cisco_ios"}
                net_connect = Netmiko(**device)
                hostname = net_connect.find_prompt()
                for command in command_list:
                    output = net_connect.send_command(command, strip_command=False)
                    print(f"{hostname} {output}\n")

                    with open(f"output/{ip} logs.txt", "a") as w:
                        w.write(f"{hostname} {output}\n\n")

        with ThreadPoolExecutor(max_workers=25) as executor:
            executor.map(concurrent, device_list)


    ################################################################################################


    def collect_device_info():
        with open("input/device_list.txt") as r:
            device_list = r.read().splitlines()

        ip_list, version_list, model_list, vendor_list, hostname_list = ([] for i in range(5))

        for ip in device_list:
            device = {"host": ip, "username": "admin", "password": "cisco", "device_type": "cisco_ios"}
            print(f"\n---Try to Login:{ip}---\n")
            net_connect = Netmiko(**device)
            output = net_connect.send_command("show version")

            version = findall("Version (.*),", output)
            model = findall("Cisco (.*)\(revision", output)
            vendor = findall("Cisco", output)
            hostname = findall("(.*)#", net_connect.find_prompt())

            ip_list.append(ip)
            version_list.append(version[0])
            model_list.append(model[0])
            vendor_list.append(vendor[0])
            hostname_list.append(hostname[0])

        df = DataFrame(
            {"IP Address": ip_list, "Hostname": hostname_list, "Vendor Type": vendor_list, "Model": model_list,
             "Version": version_list})
        df.to_excel("output/Version List.xlsx", sheet_name="Vendors", index=False)


    ################################################################################################


    def collect_cpu_usage():
        with open("input/device_list.txt") as r:
            device_list = r.read().splitlines()

        ip_list, cpu_list_5s, cpu_list_1m, cpu_list_5m, cpu_list_risk = ([] for x in range(5))

        for ip in device_list:
            device = {"host": ip, "username": "admin", "password": "cisco", "device_type": "cisco_ios"}
            print(f"\n---Try to Login:{ip}---")
            net_connect = Netmiko(**device)
            output = net_connect.send_command("show processes cpu")

            cpu_5s = findall("CPU utilization for five seconds: (\d+)", output)
            cpu_1m = findall("one minute: (\d+)", output)
            cpu_5m = findall("five minutes: (\d+)", output)

            ip_list.append(ip)
            cpu_list_5s.append(cpu_5s[0] + "%")
            cpu_list_1m.append(cpu_1m[0] + "%")
            cpu_list_5m.append(cpu_5m[0] + "%")

            if int(cpu_5m[0]) > 90:
                cpu_risk = "Fatal CPU Level"
            elif 70 < int(cpu_5m[0]) < 90:
                cpu_risk = "High CPU Level"
            else:
                cpu_risk = "No Risk"

            cpu_list_risk.append(cpu_risk)

        df = DataFrame(
            {"IP Address": ip_list, "CPU Levels for 5 Seconds": cpu_list_5s, "CPU Levels for 1 Minute": cpu_list_1m,
             "CPU Levels for 5 Minutes": cpu_list_5m, "CPU Risk": cpu_list_risk})
        df.to_excel("output/CPU Levels.xlsx", index=False)


    ################################################################################################


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


################################################################################################
################################################################################################
################################################################################################


class configure_device:
    def config_with_netmiko():
        with open("input/device_list.txt") as r:
            device_list = r.read().splitlines()

        def concurrent(ip):
            device = {"host": ip, "username": "admin", "password": "cisco", "device_type": "cisco_ios"}
            net_connect = Netmiko(**device)
            output = net_connect.send_config_from_file(config_file="input/command_list.txt", strip_command=False)
            print(output)

        with ThreadPoolExecutor(max_workers=25) as executor:
            executor.map(concurrent, device_list)


    ################################################################################################


    def config_with_nornir():
        with open("input/command_list.txt") as r:
            command_list = r.read().splitlines()

        connect = InitNornir(config_file="hosts.yaml")
        result = connect.run(task=netmiko_send_config, config_commands=command_list)
        print_result(result)

################################################################################################
################################################################################################
################################################################################################


class transfer_files:

    def scp_upload_to_routers(src_file, dest_file):
        if not dest_file:
            dest_file = src_file
        connect = InitNornir(config_file="hosts.yaml")
        result = connect.run(task=netmiko_file_transfer, source_file=src_file, dest_file=dest_file, direction="put")
        print_result(result)



    def sftp_upload_to_servers(src_file, dest_file):
        with open("input/device_list.txt") as r:
            device_list = r.read().splitlines()
        ssh = SSHClient()
        ssh.set_missing_host_key_policy(AutoAddPolicy())
        for ip in device_list:
            ssh.connect(hostname=ip, username="ubuntu", password="ubuntu")
            sftp = ssh.open_sftp()
            sftp.put(src_file,dest_file)