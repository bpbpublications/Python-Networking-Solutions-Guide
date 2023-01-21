import boto3
from netmiko import Netmiko

ec2 = boto3.resource("ec2")
instances = ec2.create_instances(
     ImageId="ami-06672d07f62285d1d",
     MinCount=1,
     MaxCount=1,
     InstanceType="t2.micro",
     KeyName="ec2-keypair"
 )

instance_id = instances[0].instance_id
print(f"{instance_id} Instance is created")

instances[0].wait_until_running()
print(f"Instance is started")

instances[0].reload()

public_ip = instances[0].public_ip_address
print(f"Public IP: {public_ip}")

device = {"host": public_ip, "username": "ec2-user", "device_type": "linux", "key_file": "ec2-keypair.pem"}
net_connect = Netmiko(**device)
output = net_connect.send_command("uptime", strip_command=False)
print(output)
