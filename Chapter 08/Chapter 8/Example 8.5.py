from netmiko import Netmiko
from getpass import getpass

host = "192.168.163.135"
device = {"host": host, "username": "ubuntu", "password": getpass(), "device_type": "linux"}
command = "uname -a"

net_connect = Netmiko(**device)
show_output = net_connect.send_command(command)
net_connect.disconnect()
print(f"{host}:{show_output}\n")
