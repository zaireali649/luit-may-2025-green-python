from helpers import *  # Import helper functions like get_ec2_client, get_s3_client, list_buckets, describe_instances

def print_bucket_names(s3_client: any) -> None:
    """
    Print the names of all S3 buckets associated with the provided S3 client.

    Args:
        s3_client (any): A boto3 S3 client object used to list buckets.

    Returns:
        None
    """
    # Retrieve the list of bucket names from the helper function
    bucket_names = list_buckets(s3_client)

    # Print each bucket name on a new line
    for bucket_name in bucket_names: # print("\n".join(bucket_names))
        print(bucket_name)


def print_instance_ids(ec2_client: any) -> None:
    """
    Print the instance IDs of all EC2 instances associated with the provided EC2 client.

    Args:
        ec2_client (any): A boto3 EC2 client object used to describe EC2 instances.

    Returns:
        None
    """
    # Retrieve the list of EC2 instances from the helper function
    instances = describe_instances(ec2_client)

    # Extract and store instance IDs in a list
    instance_ids = []
    for instance in instances:
        instance_ids.append(instance['InstanceId'])

    # Print each instance ID on a new line
    for instance_id in instance_ids:
        print(instance_id)


if __name__ == "__main__":
    # Create boto3 EC2 client using helper function
    ec2_client = get_ec2_client()
    
    # Create boto3 S3 client using helper function
    s3_client = get_s3_client()

    # Print the names of all S3 buckets
    print_bucket_names(s3_client)

    # Print the IDs of all EC2 instances
    print_instance_ids(ec2_client)
