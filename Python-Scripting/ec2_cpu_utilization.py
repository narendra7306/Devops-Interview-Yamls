# script to identify EC2 instances with CPU utilization greater than 80%

import boto3

# Create EC2 client
ec2_client = boto3.client(
    'ec2',
    region_name='ap-south-1'
)

# Create CloudWatch client
cloudwatch_client = boto3.client(
    'cloudwatch',
    region_name='ap-south-1'
)

# Get all running EC2 instances
response = ec2_client.describe_instances(
    Filters=[
        {
            'Name': 'instance-state-name',
            'Values': ['running']
        }
    ]
)

# Iterate through reservations and instances
for reservation in response['Reservations']:
    for instance in reservation['Instances']:

        instance_id = instance['InstanceId']

        # Get CPU utilization from CloudWatch
        metrics = cloudwatch_client.get_metric_statistics(
            Namespace='AWS/EC2',
            MetricName='CPUUtilization',
            Dimensions=[
                {
                    'Name': 'InstanceId',
                    'Value': instance_id
                }
            ],
            StartTime=datetime.datetime.now(
                datetime.timezone.utc
            ) - datetime.timedelta(minutes=10),
            EndTime=datetime.datetime.now(
                datetime.timezone.utc
            ),
            Period=300,
            Statistics=['Average']
        )

        datapoints = metrics['Datapoints']

        if datapoints:
            cpu_usage = datapoints[-1]['Average']

            if cpu_usage > 80:
                print(
                    f"High CPU Alert: {instance_id}, "
                    f"CPU Usage: {cpu_usage:.2f}%"
                )

