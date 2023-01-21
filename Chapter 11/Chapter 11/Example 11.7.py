from netmiko import Netmiko

device = {"host": "18.170.25.70", "username": "ec2-user", "device_type": "linux", "key_file": "ec2-keypair.pem"}

net_connect = Netmiko(**device)
output = net_connect.send_command("uname -a", strip_command=False)

print(output)
