from jinja2 import Environment, FileSystemLoader
from yaml import safe_load
from netmiko import Netmiko
import re

ip = {"host": "10.10.10.1", "username": "admin", "password": "cisco", "device_type": "cisco_ios", "global_delay_factor": 0.1}

env = Environment(loader=FileSystemLoader("."))
template = env.get_template("commands.txt")

with open("info.yml") as r:
    data = safe_load(r)

command = template.render(data)

command = re.split("\n", command)

print(f"\n---Try to Login: {ip['host']} ---\n")
net_connect = Netmiko(**ip)
output = net_connect.send_config_set(command)
print(output)
