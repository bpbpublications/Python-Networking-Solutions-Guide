import boto3

ec2 = boto3.resource("ec2")
new_volume = ec2.create_volume(AvailabilityZone="eu-west-2a", Size=20)

print(f"Created volume ID: {new_volume.id}")
