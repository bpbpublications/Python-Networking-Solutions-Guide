import boto3

s3 = boto3.resource("s3")

def create_bucket (bucket_name):
    s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={
    "LocationConstraint": "eu-west-2"})

def delete_bucket (bucket_name):
    bucket = s3.Bucket(bucket_name)
    bucket.delete()

create_bucket("test-storage-python-1")
