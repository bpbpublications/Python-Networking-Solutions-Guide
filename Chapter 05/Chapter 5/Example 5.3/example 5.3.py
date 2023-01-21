import xlwings
from netmiko import Netmiko

excel = xlwings.Book("Config_file.xlsx").sheets['Sheet1']
column = ["A","B","C"]
host = ["10.10.10.1", "10.10.10.2", "10.10.10.3"]

for x,ip in zip(column,host):
    print(f"---Connected to {ip}---")
    configuration = excel.range(f"{x}1:{x}14").value
    device = {"host": ip, "username": "admin", "password": "cisco","device_type": "cisco_ios"}
    net_connect = Netmiko(**device)
    net_connect.send_config_set(configuration)
