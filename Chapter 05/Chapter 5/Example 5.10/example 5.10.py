from jinja2 import Environment, FileSystemLoader
from yaml import safe_load
from netmiko import Netmiko
import re

ip_list = [ "10.10.10.1", "10.10.10.2", "10.10.10.3" ]

env = Environment(loader=FileSystemLoader("."))
template = env.get_template("commands.txt")

with open("info.yml") as r:
    data = safe_load(r)

for x,ip in zip(data,ip_list):
        ip = {
            "host": f"{ip}",
            "username": "admin",
            "password": "cisco",
            "device_type": "cisco_ios",
            "global_delay_factor": 0.1}
        command = template.render(x)
        command = re.split("\n", command)
        print(f"\n---Try to Login: {ip['host']} ---\n")
        net_connect = Netmiko(**ip)
        output = net_connect.send_config_set(command)
        print(output)
