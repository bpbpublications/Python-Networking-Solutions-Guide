import boto3

ec2 = boto3.resource("ec2")
volume_id = "vol-0ae620def39c1c379"

snapshot_volume = ec2.create_snapshot(VolumeId=volume_id)

print(f"Original Volume: {volume_id} \nSnapshot Volume: {snapshot_volume.id}")
