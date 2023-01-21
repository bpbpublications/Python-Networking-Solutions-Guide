from netmiko import Netmiko

host = ["192.168.163.135", "192.168.163.136", "192.168.163.137"]
for ip in host:
    device = {"host": ip, "username": "ubuntu", "password": "ubuntu", "device_type": "linux"}
    command = "uname -a"

    net_connect = Netmiko(**device)
    output = net_connect.send_command(command, strip_command=False)
    net_connect.disconnect()
    print(f"{ip}:{output}\n")

Output:
192.168.163.135:uname -a
Linux Server-1 5.15.0-47-generic #51-Ubuntu SMP Thu Aug 11 07:51:15 UTC 2022 x86_64 x86_64 x86_64 GNU/Linux

192.168.163.136:uname -a
Linux Server-2 5.15.0-47-generic #51-Ubuntu SMP Thu Aug 11 07:51:15 UTC 2022 x86_64 x86_64 x86_64 GNU/Linux

192.168.163.137:uname -a
Linux Server-3 5.15.0-47-generic #51-Ubuntu SMP Thu Aug 11 07:51:15 UTC 2022 x86_64 x86_64 x86_64 GNU/Linux
