from netmiko import Netmiko
from re import findall, split
from jinja2 import Environment, FileSystemLoader
from yaml import safe_load

host = ["192.168.163.135", "192.168.163.136", "192.168.163.137"]

env = Environment(loader=FileSystemLoader("."))
template = env.get_template("command_list.txt")
with open("info.yml") as r:
    data = safe_load(r)
    user_name = data["user_name"]

command = template.render(data)
command = split("\n", command)

for ip in host:
    device = {"host": ip, "username": "ubuntu", "password": "ubuntu", "device_type": "linux", "secret": "ubuntu"}
    net_connect = Netmiko(**device)
    output = net_connect.send_config_set(command)
    hostname = findall("@(.*):", net_connect.find_prompt())
    result = findall("uid",output)

    if result:
        uid = findall("uid=(.*) gid",output)
        gid = findall("gid=(.*) ",output)
        groups = findall("groups=(.*)",output)
        print(f"{hostname[0]}: User '{user_name}' is created and assigned to a group")
        print(f"UID: {uid[0]} \nGID: {gid[0]} \nGroups: {groups[0]}\n")
    else:
        print("Failed to create user and group")
