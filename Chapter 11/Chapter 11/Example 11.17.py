import boto3

def add_role(username,role_name):
    policy_arn = f"arn:aws:iam::aws:policy/{role_name}"
    iam = boto3.resource("iam")
    iam.User(username).attach_policy(PolicyArn=policy_arn)

def remove_role(username,role_name):
    policy_arn = f"arn:aws:iam::aws:policy/{role_name}"
    iam = boto3.resource("iam")
    iam.User(username).detach_policy(PolicyArn=policy_arn)

add_role("abcd","AmazonEC2FullAccess")
