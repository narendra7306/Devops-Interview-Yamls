# Python script to list all EC2 instances in an AWS account

import boto3

# Create EC2 client
ec2_client = boto3.client(
    'ec2',
    region_name='ap-south-1'
)

# Get EC2 instances
response = ec2_client.describe_instances()

# Iterate through reservations and instances
for reservation in response['Reservations']:
    for instance in reservation['Instances']:

        print("Instance ID:", instance['InstanceId'])
        print("Instance Type:", instance['InstanceType'])
        print("Instance State:", instance['State']['Name'])
        print("-" * 40)

