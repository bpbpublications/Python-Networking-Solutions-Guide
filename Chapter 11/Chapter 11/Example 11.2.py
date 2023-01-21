import boto3

ec2 = boto3.resource("ec2")
instances = ec2.create_instances(
     ImageId="ami-06672d07f62285d1d",
     MinCount=1,
     MaxCount=3,
     InstanceType="t2.micro",
     KeyName="ec2-keypair"     )
