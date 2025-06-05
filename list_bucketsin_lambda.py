import json
import boto3  # AWS SDK for Python; used to interact with AWS services

def list_buckets(s3_client):
    response = s3_client.list_buckets()  # Call the S3 API to list all buckets in the account

    buckets = response['Buckets']  # Extract the list of buckets from the response

    bucket_names = []  # Initialize an empty list to store bucket names

    for bucket in buckets:  # Loop through each bucket in the list
        if "Name" in bucket:  # Check if the 'Name' key exists in the bucket dictionary
            bucket_names.append(bucket['Name'])  # Add the bucket name to the list

    return bucket_names

def lambda_handler(event, context):
    s3 = boto3.client('s3')  # Create an S3 client using default AWS credentials and region

    bucket_names = list_buckets(s3)

    for bucket_name in bucket_names:
        print(bucket_name)  # Print the name of the bucket

    return {
        'statusCode': 200,  # Return a successful HTTP status code
        'body': json.dumps(bucket_names)
    }


if __name__=="__main__":
    lambda_handler(None, None)
