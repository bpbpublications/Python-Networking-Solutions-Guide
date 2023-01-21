from netmiko import Netmiko
from concurrent.futures import ThreadPoolExecutor

host = ["192.168.163.135", "192.168.163.136", "192.168.163.137"]

def package_installation (ip):
    device = {"host": ip, "username": "ubuntu", "password": "ubuntu", "device_type": "linux", "secret": "ubuntu"}
    package = ["htop","nano", "vim", "nmap"]

    for pack in package:
        net_connect = Netmiko(**device)
        net_connect.send_config_set(f"sudo apt-get install {pack} -y")
        output = net_connect.send_command(f"{pack} --version")
        hostname = net_connect.find_prompt()
        print(f"{hostname}: {pack} --version{output}\n")
        net_connect.disconnect()

with ThreadPoolExecutor(max_workers=5) as executor:
    result = executor.map(package_installation, host)
