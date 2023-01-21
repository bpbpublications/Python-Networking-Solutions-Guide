from netmiko import Netmiko
import re

device1 = {"host": "10.10.10.1", "username": "admin", "password": "cisco", "device_type": "cisco_ios", "global_delay_factor": 0.1}
device2 = {"host": "10.10.10.2", "username": "admin", "password": "cisco", "device_type": "cisco_ios", "global_delay_factor": 0.1}
device3 = {"host": "10.10.10.3", "username": "admin", "password": "cisco", "device_type": "cisco_ios", "global_delay_factor": 0.1}
host = [device1, device2, device3]

check_ip = "10.10.10.2"
duplicated_list = []
command = "show ip interface brief"

for ip in host:
    print(f"\n---Try to Login: {ip['host']} ---\n")
    try:
        net_connect = Netmiko(**ip)
        output =net_connect.send_command(command)
        duplicate_ip = re.findall(check_ip,output)

        while duplicate_ip:
            interface = re.findall(f"(.*){check_ip}",output)
            duplicated_list.append(check_ip)
            duplicate_device = ip["host"]
            break
    except:
        print(f"***Cannot login to {ip['host']}")

if duplicated_list:
    print(f"---------\nDuplicated IP: {check_ip} \nDuplicated Device IP Address: {duplicate_device} \nInterface: {interface[0]} \n -----------")
else:
    print(f"{check_ip} IP address is suitable for use")