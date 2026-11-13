
import boto3

# Connect to EC2
ec2 = boto3.client('ec2', region_name='ap-south-1')

# Get stopped instances
response = ec2.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['stopped']}])

# Print stopped instance IDs
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        print("Stopped Instance:", instance['InstanceId'])
