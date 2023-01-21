import boto3

s3 = boto3.resource("s3")
source= { "Bucket" : "test-storage-python-1", "Key": "test.txt"}
destination = s3.Bucket("test-storage-python-2")
destination.copy(source, "test.txt")
