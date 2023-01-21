import boto3

ec2 = boto3.resource("ec2")

instance_data = ec2.instances.all()

for info in instance_data:
    print("-"*20,f"\nEC2 instance ID: {info.id}")
    print(f"Instance State: {info.state['Name']}")
    print(f"Instance Public IP: {info.public_ip_address}")
    print(f"Instance AMI: {info.image.id}")
    print(f"Instance Type: {info.instance_type}")
print("-"*20,"\n")
