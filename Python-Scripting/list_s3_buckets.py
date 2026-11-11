# Python script using Boto3  Retrieve all S3 buckets, Identify buckets that have versioning enabled.
# Identify buckets that have versioning disabled or suspended. Print the bucket name and its versioning status.

import boto3

# Create S3 client
s3 = boto3.client('s3', region_name='ap-south-1')

# Get all S3 buckets
response = s3.list_buckets()

# Iterate through buckets
for bucket in response['Buckets']:

    bucket_name = bucket['Name']

    # Check bucket versioning
    versioning = s3.get_bucket_versioning(
        Bucket=bucket_name
    )

    status = versioning.get('Status', 'Disabled')

    print("Bucket Name:", bucket_name)
    print("Versioning Status:", status)
    print("-" * 40)

    