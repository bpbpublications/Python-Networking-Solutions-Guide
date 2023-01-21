import paramiko
from time import sleep
import re
import threading

def SSH_Thread():
    with open("ip_list.txt") as r:
        host = r.read()
    host = re.split("\n", host)

    for ip in host:
        trd = threading.Thread(target=ssh_conn, args=(ip,))
        trd.start()

def ssh_conn(ip):
    with open("command_list.txt") as c:
        command_list = c.read()
    command_list = re.split("\n", command_list)

    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, 22, "admin", "cisco")
    commands = client.invoke_shell()
    result = ""

    for comm in command_list:
        commands.send(f"{comm} \n")
        sleep(1.5)
        output = commands.recv(1000000).decode("utf-8").replace("\r", "")
        result += str(output)
        print(output)

    with open(f"{ip}.log", "a") as wr:
        wr.write(result)

SSH_Thread()