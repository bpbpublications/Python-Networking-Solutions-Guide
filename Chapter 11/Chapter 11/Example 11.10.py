import boto3

bucket_name = "test-storage-python-1"
local_file = "test.txt"
file_on_bucket = "test.txt"

s3 = boto3.resource("s3")
s3_object = s3.Object(bucket_name, file_on_bucket)

def uploading(local_file):
    s3_object.upload_file(local_file)

def downloading(local_file):
    s3_object.download_file(local_file)

def deleting():
    s3_object.delete()
print("S3 object deleted")

uploading(local_file)
