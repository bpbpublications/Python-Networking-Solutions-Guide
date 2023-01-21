from netmiko import Netmiko
from re import findall,split

device = {"host": "192.168.163.135", "username": "ubuntu", "password": "ubuntu", "device_type": "linux"}
net_connect = Netmiko(**device)
output = split("\n",net_connect.send_command("ls -l"))
del output[:2]

for item in output:
    file_name = findall("\d+:\d+ (.*)",item)
    print(f"File/Directory Name: {file_name[0]}")
    if item[0] == "d":
        print("Type: Directory")
    else:
        print("Type: File")

    if item[1:4] == "r--":
        print(f"User Permission: Read as '{item[1:4]}'\n")
    elif item[1:4] == "rw-":
        print(f"User Permission: Read/Write as '{item[1:4]}'\n")
    elif item[1:4] == "rwx":
        print(f"User Permission: Read/Write/Execute as '{item[1:4]}'\n")
    elif item[1:4] == "---":
        print(f"User Permission: None as '{item[1:4]}'\n")
