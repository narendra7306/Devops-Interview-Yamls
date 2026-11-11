
import boto3

# Connect to IAM
iam = boto3.client('iam')

# Get IAM users
users = iam.list_users()

# Print usernames
for user in users['Users']:
    print(user['UserName'])
