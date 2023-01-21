from paramiko import SSHClient, AutoAddPolicy
from time import sleep

host = ["192.168.163.135", "192.168.163.136", "192.168.163.137"]

for ip in host:
    client = SSHClient()
    client.set_missing_host_key_policy(AutoAddPolicy())
    client.connect(hostname=ip, username="ubuntu", password="ubuntu")
    commands = client.invoke_shell()
    commands.send("hostnamectl hostname\n")
    sleep(1)

    output = commands.recv(1000000).decode("utf-8")
    print(f"\n\n-------------------\nConnected to: {ip}\n-------------------\n{output}")
