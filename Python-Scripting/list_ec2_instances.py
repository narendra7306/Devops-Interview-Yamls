
import boto3

# Connect to EC2
ec2 = boto3.client('ec2', region_name='ap-south-1')

# Get EC2 instances
response = ec2.describe_instances()

# Print instance details
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        print("Instance ID:", instance['InstanceId'])
        print("Instance Type:", instance['InstanceType'])
        print("State:", instance['State']['Name'])
        print("-" * 30)
