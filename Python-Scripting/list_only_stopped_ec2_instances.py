# python script to list only stopped ec2 instances

import boto3

ec2_client = boto3.client(
    'ec2',
    region_name='ap-south-1'
)

response = ec2_client.describe_instances(
    Filters=[
        {
            'Name': 'instance-state-name',
            'Values': ['stopped']
        }
    ]
)

for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        print("Stopped Instance:", instance['InstanceId'])

