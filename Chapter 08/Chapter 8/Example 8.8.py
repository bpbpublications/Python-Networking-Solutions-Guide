from netmiko import Netmiko
from re import findall
from pandas import DataFrame

list_ipv4, list_netmask, list_int, list_hostname, list_int_name = ([] for i in range(5))
host = ["192.168.163.135", "192.168.163.136", "192.168.163.137"]

for ip in host:
    device = {"host": ip, "username": "ubuntu", "password": "ubuntu", "device_type": "linux"}
    net_connect = Netmiko(**device)
    output = net_connect.send_command("ifconfig")
    hostname = findall("@(.*):", net_connect.find_prompt())
    int_name = findall("(.*): flags", output)

    for interface in int_name:
        output = net_connect.send_command(f"ifconfig -a {interface}")
        ipv4 = findall("inet (.*)  netmask", output)
        netmask = findall("netmask (\d+.\d+.\d+.\d+)", output)
        list_ipv4.append(ipv4[0])
        list_netmask.append(netmask[0])
        list_hostname.append(hostname[0])
        list_int_name.append(interface)

df = DataFrame({"Hostname": list_hostname, "Interface Name": list_int_name, "IP Address": list_ipv4, "Netmask": list_netmask, })
df.to_excel("Interface Information.xlsx", index=False)
