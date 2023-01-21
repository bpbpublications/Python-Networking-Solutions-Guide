from concurrent.futures import ThreadPoolExecutor
from netmiko import Netmiko, file_transfer, progress_bar

def get_ip_address():
    with open("device_list.txt") as r:
        host_list = r.read().splitlines()
    return host_list

def netmiko_scp(ip):
    host = {"ip": ip, "username": "admin", "password": "cisco", "device_type": "cisco_ios"}
    print(f"---Try to Login:{ip}---")
    net_connect = Netmiko(**host)
    file_transfer(net_connect,
                  source_file="test.txt",
                  dest_file="test.txt",
                  direction="put",
                  file_system="flash:",
                  overwrite_file=True,
                  progress4=progress_bar)
    net_connect.disconnect()
    return

with ThreadPoolExecutor(max_workers=25) as executor:
    host_ip = get_ip_address()
    result = executor.map(netmiko_scp, host_ip)
