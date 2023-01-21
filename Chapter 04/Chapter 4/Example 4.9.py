from netmiko import Netmiko
import re
from pandas import DataFrame

device1 = {"host": "10.10.10.1", "username": "admin", "password": "cisco",
           "device_type": "cisco_ios", "global_delay_factor": 0.1}
device2 = {"host": "10.10.10.2", "username": "admin", "password": "cisco",
           "device_type": "cisco_ios", "global_delay_factor": 0.1}
device3 = {"host": "10.10.10.3", "username": "admin", "password": "cisco",
           "device_type": "cisco_ios", "global_delay_factor": 0.1}
host = [device1, device2, device3]
command = "show version"

ip_list, version_list, model_list, vendor_list, hostname_list = ([] for i in range(5))

for ip in host:

    try:
        print(f"\n---Try to Login:{ip['host']}---\n")
        net_connect = Netmiko(**ip)
        output = net_connect.send_command(command)
        print(output)

        version = re.findall("Version (.*),", output)
        model = re.findall("Cisco (.*)\(revision", output)
        vendor = re.findall("Cisco", output)
        hostname = re.findall("(.*) uptime is", output)

        ip_list.append(ip['host'])
        version_list.append(version[0])
        model_list.append(model[0])
        vendor_list.append(vendor[0])
        hostname_list.append(hostname[0])

    except:
        print(f"***Cannot login to {ip['host']}")

df = DataFrame({"IP Address": ip_list, "Hostname": hostname_list, "Vendor Type": vendor_list, "Model": model_list, "Version": version_list})
df.to_excel("Version List.xlsx", sheet_name="Vendors", index=False)