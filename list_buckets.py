import boto3  # AWS SDK for Python; used to interact with AWS services

s3 = boto3.client('s3')  # Create an S3 client using default AWS credentials and region

response = s3.list_buckets()  # Call the S3 API to list all buckets in the account

buckets = response['Buckets']  # Extract the list of buckets from the response

for bucket in buckets:  # Loop through each bucket in the list
    if "Name" in bucket:  # Check if the 'Name' key exists in the bucket dictionary
        print(bucket['Name'])  # Print the name of the bucket
