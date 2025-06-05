import json
import boto3  # AWS SDK for Python; used to interact with AWS services

def lambda_handler(event, context):
    s3 = boto3.client('s3')  # Create an S3 client using default AWS credentials and region

    response = s3.list_buckets()  # Call the S3 API to list all buckets in the account

    buckets = response['Buckets']  # Extract the list of buckets from the response

    bucket_names = []  # Initialize an empty list to store bucket names

    for bucket in buckets:  # Loop through each bucket in the list
        if "Name" in bucket:  # Check if the 'Name' key exists in the bucket dictionary
            print(bucket['Name'])  # Print the name of the bucket
            bucket_names.append(bucket['Name'])  # Add the bucket name to the list

    return {
        'statusCode': 200,  # Return a successful HTTP status code
        'body': json.dumps(bucket_names)
    }


if __name__=="__main__":
    lambda_handler(None, None)
