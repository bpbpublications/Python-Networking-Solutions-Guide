import boto3

ec2_resource = boto3.resource("ec2")
volume = ec2_resource.Volume("vol-0ae620def39c1c379")
print(f"Volume: {volume.id}   Status: {volume.state}")

volume.attach_to_instance(Device="/dev/sdh", InstanceId="i-0d1d8dd7bc1887539")

print(f"Volume: {volume.id}   Status: {volume.state}")
