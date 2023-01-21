from netmiko import Netmiko
from re import findall
from concurrent.futures import ThreadPoolExecutor

host = ["10.10.10.1", "10.10.10.2", "10.10.10.3"]

def collect_cpu(ip):
    device = {"host": ip, "username": "admin", "password": "cisco", "device_type": "cisco_ios"}
    command = "show run"
    net_connect = Netmiko(**device)
    output = net_connect.send_command(command)
    username = findall("username.*",output)

    for user in username:
        secret = findall("secret", user)
        username = findall("username (\S+) ",user)
        if secret:
            print(f"{ip}: '{username[0]}' has a secret password. It's SECURE")
        else:
            print(f"{ip}: '{username[0]}' has no secret password. It's INSECURE")

with ThreadPoolExecutor(max_workers=50) as executor:
    result = executor.map(collect_cpu, host)
