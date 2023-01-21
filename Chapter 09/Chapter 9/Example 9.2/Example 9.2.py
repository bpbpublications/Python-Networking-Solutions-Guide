from netmiko import Netmiko
from re import split
from jinja2 import Environment, FileSystemLoader
from yaml import safe_load

def from_jinja():
    env = Environment(loader=FileSystemLoader("."))
    template = env.get_template("command_list.txt")
    with open("info.yml") as r:
        data = safe_load(r)
    command = split("\n", template.render(data))
    return [command, data]

def add_zone(ip):
    device = {"host": ip, "username": "ubuntu", "password": "ubuntu", "device_type": "linux", "secret": "ubuntu"}
    net_connect = Netmiko(**device)
    commands = from_jinja()[0]
    net_connect.send_config_set(commands, read_timeout=1000)
    return net_connect

def zone_configuration(ip):
    interface = "lo"
    data = from_jinja()[1]
    new_zone = data["new_zone"]
    commands = [f"firewall-cmd --permanent --zone={new_zone} --change-interface={interface}",
                "firewall-cmd --reload",
                "firewall-cmd --get-active-zones",
                f"sudo firewall-cmd --zone={new_zone} --add-service=http",
                f"sudo firewall-cmd --zone={new_zone} --add-port=80/tcp",
                f"firewall-cmd --zone={new_zone} --add-forward-port=port=80:proto=udp:toport=8080:toaddr=10.10.10.1"
                ]

    connect = add_zone(ip)
    connect.send_config_set(commands)
    out=connect.send_config_set(f"sudo firewall-cmd --list-all --zone={new_zone}")
    print(out)

zone_configuration("192.168.163.135")
