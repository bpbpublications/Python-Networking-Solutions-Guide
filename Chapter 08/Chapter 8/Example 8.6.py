from netmiko import Netmiko
from getpass import getpass

host = ["192.168.163.135", "192.168.163.136", "192.168.163.137"]
command = "uname -a"
password = getpass()

for ip in host:
    device = {"host": ip, "username": "ubuntu", "password": password, "device_type": "linux"}
    net_connect = Netmiko(**device)
    show_output = net_connect.send_command(command)
    net_connect.disconnect()
    print(f"{ip}:{show_output}\n")
