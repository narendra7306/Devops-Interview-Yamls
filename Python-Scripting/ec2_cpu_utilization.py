
import boto3
from datetime import datetime, timedelta, timezone

# Create EC2 and CloudWatch clients
ec2 = boto3.client('ec2', region_name='ap-south-1')
cw = boto3.client('cloudwatch', region_name='ap-south-1')

# Get running EC2 instances
response = ec2.describe_instances(
    Filters=[{'Name': 'instance-state-name', 'Values': ['running']}]
)

# Check CPU utilization
for reservation in response['Reservations']:
    for instance in reservation['Instances']:

        instance_id = instance['InstanceId']

        metrics = cw.get_metric_statistics(
            Namespace='AWS/EC2',
            MetricName='CPUUtilization',
            Dimensions=[{'Name': 'InstanceId', 'Value': instance_id}],
            StartTime=datetime.now(timezone.utc) - timedelta(minutes=10),
            EndTime=datetime.now(timezone.utc),
            Period=300,
            Statistics=['Average']
        )

        if metrics['Datapoints']:
            cpu = metrics['Datapoints'][-1]['Average']

            if cpu > 80:
                print(f"ALERT: {instance_id} CPU is {cpu:.2f}%")
