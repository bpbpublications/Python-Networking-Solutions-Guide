import boto3

iam = boto3.resource("iam")
result = iam.create_user(UserName="abcd")
print(result)
