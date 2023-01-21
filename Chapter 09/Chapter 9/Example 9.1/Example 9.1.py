from netmiko import Netmiko
from concurrent.futures import ThreadPoolExecutor

host = ["192.168.163.135", "192.168.163.136", "192.168.163.137"]

def server_connection(ip):
    device = {"host": ip, "username": "ubuntu", "password": "ubuntu", "device_type": "linux", "secret": "ubuntu"}
    net_connect = Netmiko(**device)
    return net_connect

def start_firewalld(ip):
    connection = server_connection(ip)
    output = connection.send_config_from_file("start_firewalld.txt", read_timeout=1000)
    print(output)

def stop_firewalld(ip):
    connection = server_connection(ip)
    output = connection.send_config_from_file("stop_firewalld.txt", read_timeout=1000)
    print(output)

def disable_service_on_boot(ip):
    service = "firewalld"
    connection = server_connection(ip)
    connection.send_config_set(f"systemctl disable {service}", read_timeout=1000)
    output = connection.send_command(f"systemctl list-unit-files --type=service | grep {service}")
    print(output)

def enable_service_on_boot(ip):
    service = "firewalld"
    connection = server_connection(ip)
    connection.send_config_set(f"systemctl enable {service}", read_timeout=1000)
    output = connection.find_prompt() + connection.send_command(f"systemctl list-unit-files --type=service | grep {service}")
    print(output)

with ThreadPoolExecutor(max_workers=5) as executor:
    result = executor.map(enable_service_on_boot, host)
