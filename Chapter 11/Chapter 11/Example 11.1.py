import boto3
ec2 = boto3.resource("ec2")

key_pair = ec2.create_key_pair(KeyName="ec2-keypair")
output = str(key_pair.key_material)

with open("ec2-keypair.pem","w") as wr:
        wr.write(output)
