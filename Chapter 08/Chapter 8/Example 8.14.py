from netmiko import Netmiko
from re import findall
from concurrent.futures import ThreadPoolExecutor

host = ["192.168.163.135", "192.168.163.136", "192.168.163.137"]
command = "reboot"

def netmiko_reboot(ip):
    device = {"host": ip, "username": "ubuntu", "password": "ubuntu", "device_type": "linux", "secret": "ubuntu"}
    net_connect = Netmiko(**device)
    hostname = findall("@(.*):", net_connect.find_prompt())
    print(f"---Rebooting to:{hostname}---")
    net_connect.send_config_set(command)
    return

with ThreadPoolExecutor(max_workers=5) as executor:
    result = executor.map(netmiko_reboot, host)
