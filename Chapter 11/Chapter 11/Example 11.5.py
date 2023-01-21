import boto3

instance_id = "i-0aabe4b7adb32fd87" #Enter your instance ID in string
ec2 = boto3.resource("ec2")

instance = ec2.Instance(instance_id)
print(f"Instance ID: {instance_id} \nCurrent Instance Type: {instance.instance_type}")

instance.stop()
print("---\nInstance is stopping")
instance.wait_until_stopped()
print("---\nInstance is stopped")

instance.modify_attribute(InstanceType={"Value": "t2.small"})
print("---\nInstance type is changed")

instance.start()
print("---\nInstance is starting")
instance.wait_until_running()
print(f"---\nInstance started with the new instance type.")
print(f"Instance ID: {instance_id} \nCurrent Instance Type: {instance.instance_type}")
