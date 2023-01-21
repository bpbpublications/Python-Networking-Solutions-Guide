from netmiko import Netmiko
import re

with open("host_info.txt") as r:
    host = r.read()
ip_list = re.split("\n", host)

for ip in ip_list:
    ip = {
        "host": f"{ip}",
        "username":"admin",
        "password":"cisco",
        "device_type": "cisco_ios",
        "global_delay_factor": 0.1
    }

    try:
        print(f"\n---Try to Login: {ip['host']} ---\n")
        net_connect = Netmiko(**ip)
        output = net_connect.send_command("show interface description")
        print(output)
    except:
        print(f"***Cannot login to {ip['host']}")
