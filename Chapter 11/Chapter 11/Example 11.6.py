from paramiko import SSHClient, AutoAddPolicy
from time import sleep

client = SSHClient()
client.set_missing_host_key_policy(AutoAddPolicy())
client.connect(hostname="PUBLIC IP_OR_DNS", username="ec2-user", key_filename= "ec2-keypair.pem")

commands = client.invoke_shell()
commands.send("uname -a \n")
sleep(1)

output = commands.recv(1000000)
output = output.decode("utf-8")
client.close()
print(output)print("---\nInstance type is changed")

instance.start()
print("---\nInstance is starting")
instance.wait_until_running()
print(f"---\nInstance started with the new instance type.")
print(f"Instance ID: {instance_id} \nCurrent Instance Type: {instance.instance_type}")
