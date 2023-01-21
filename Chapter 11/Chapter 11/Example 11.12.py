import boto3

bucket_name = "test-storage-python-1"
s3 = boto3.resource("s3")
s3_bucket = s3.Bucket(bucket_name)

for item in s3_bucket.objects.all():
    print(f"{item.key} - Size: {item.size} Bytes")
