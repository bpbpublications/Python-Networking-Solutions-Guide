from netmiko import Netmiko

host = ["192.168.163.135", "192.168.163.136", "192.168.163.137"]
for ip in host:
    device = {"host": ip, "username": "ubuntu", "password": "ubuntu", "device_type": "linux"}
    command = "cat /var/log/syslog"
    net_connect = Netmiko(**device)
    output = net_connect.send_command(command)
    net_connect.disconnect()
    with open (f"{ip} syslog.txt","a") as w:
        w.write(output)
