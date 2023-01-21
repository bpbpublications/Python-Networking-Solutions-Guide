import paramiko
import time

hosts = ["10.10.10.1","10.10.10.2","10.10.10.3"]
command_list = ["conf t","int g0/0","description NEW-TEST"]

for ip in hosts:
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect (ip,22,"admin","cisco")
    commands = client.invoke_shell()

    for command in command_list:
        commands.send("{} \n".format(command))
        time.sleep(1)
        output = commands.recv(1000000)
        output = output.decode("utf-8")
        print (output)