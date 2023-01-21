import boto3
from InquirerPy import inquirer

def ec2_start():
     instance.start()
     print(f"Starting EC2 instance: {instance.id}")
     instance.wait_until_running()
     print(f"----\nEC2 Instance ID: {instance.id} \nStatus: Started")


def ec2_stop():
     instance.stop()
     print(f"Stopping EC2 instance: {instance.id}")
     instance.wait_until_stopped()
     print(f"----\nEC2 Instance ID: {instance.id} \nStatus: Stopped")

def ec2_reboot():
     instance = ec2.Instance(instance_id)
     instance.reboot()
     print(f"----\nEC2 Instance ID: {instance.id} \nStatus: Rebooted")

def ec2_terminate():
     instance.terminate()
     print(f"Terminating EC2 instance: {instance.id}")
     instance.wait_until_terminated()
     print(f"----\nEC2 Instance ID: {instance.id} \nStatus: Terminated")

instance_id = input("Enter Instance ID: ")
main_task = inquirer.select(
    message="Choose action for Instance:",
    choices=["Start EC2 Instance", "Stop EC2 Instance", "Reboot EC2 Instance", "Terminate EC2 Instance", "Exit"]).execute()

ec2 = boto3.resource("ec2")
instance = ec2.Instance(instance_id)

if main_task == "Start EC2 Instance":
     ec2_start()
elif main_task == "Stop EC2 Instance":
     ec2_stop()
elif main_task == "Reboot EC2 Instance":
     ec2_reboot()
elif main_task == "Terminate EC2 Instance":
     ec2_terminate()
elif main_task == "Exit":
     print("Exit from the task.")
