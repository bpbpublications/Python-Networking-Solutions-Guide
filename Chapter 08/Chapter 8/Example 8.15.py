from netmiko import Netmiko
from re import findall

host = ["192.168.163.135", "192.168.163.136", "192.168.163.137"]
for ip in host:
    device = {"host": ip, "username": "ubuntu", "password": "ubuntu", "device_type": "linux"}
    command = "ps fax"
    process = "gnome-calculator"

    net_connect = Netmiko(**device)
    output = net_connect.send_command(command)
    hostname = findall("@(.*):", net_connect.find_prompt())
    pid = findall(f"(\d+).*{process}", output)

    if pid:
        net_connect.send_command(f"kill {pid[0]}")
        output = net_connect.send_command(command)
        pid_new = findall(f"(\d+).*{process}", output)

        if not pid_new:
            print(f"{hostname[0]}  '{process}' with {pid[0]} process-id is successfully stopped.")
        else:
            print(f"{hostname[0]}  '{process}' with {pid[0]} process-id is failed stopped.")

    else:
        print(f"{hostname[0]}  '{process}' process is not started.")
