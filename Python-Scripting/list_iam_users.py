# python script to list IAM users of AWS account

import boto3

# Connect to AWS IAM
iam_client = boto3.client(
    'iam',
    region_name='ap-south-1'
)

# List IAM users
response = iam_client.list_users()

for user in response['Users']:
    print(user['UserName'])

