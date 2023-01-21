from netmiko import Netmiko
from re import findall
from concurrent.futures import ThreadPoolExecutor

host = ["10.10.10.1", "10.10.10.2", "10.10.10.3"]

def collect_cpu(ip):
    device = {"host": ip, "username": "admin", "password": "cisco", "device_type": "cisco_ios"}
    command = "show ip interface brief"
    net_connect = Netmiko(**device)
    output = net_connect.send_command(command)
    interfaces = findall("GigabitEthernet.*",output)
    for port in interfaces:
        int_name = findall("(GigabitEthernet\d+/\d+)", port)
        port_shutdown = findall("administratively down", port)
        port_up = findall("up\s+up", port)
        if not port_shutdown and not port_up:
            print(f"{ip}: '{int_name[0]}' is 'no shutdown' There is a risk")

with ThreadPoolExecutor(max_workers=50) as executor:
    result = executor.map(collect_cpu, host)
